from z3 import *

def int2bytes(a):# int -> bytes:
    #return a.to_bytes(16, byteorder='little')
    return ('%%0%dx' % (16 << 1) % a).decode('hex')[-16:][::-1]

def combine128(a, b):
    return (a << 64) | b

def edx2xmm5(e):
    return combine128(e & 0xffff, (e & 0xffff0000) >> 16)

xmm5_results = [
    0x220f02c883fbe083c0200f10cd0013b8,
    edx2xmm5(0x02df028f),
    edx2xmm5(0x0290025d),
    edx2xmm5(0x02090221),
    edx2xmm5(0x027b0278),
    edx2xmm5(0x01f90233),
    edx2xmm5(0x025e0291),
    edx2xmm5(0x02290255),
    edx2xmm5(0x02110270),
]

# Z3 Solve here

def int2bitvecval(x):
    return [BitVecVal(ord(i), 16) for i in int2bytes(x)]

def andps_z3(a, b):
    assert len(a) == len(b) == 16
    r = []
    for i in range(16):
        r.append(a[i] & b[i])
    return r

def abs_z3(x):
    return If(x >= 0, x, -x)

def psadbw_z3(a, b):
    assert len(a) == len(b) == 16
    t = [BitVecVal(0, 16) for _ in range(16)]
    for i in range(16):
        t[i] = abs_z3(a[i] - b[i])

    s1 = Sum(t[0:8])
    s2 = Sum(t[8:])
    r = [BitVecVal(0, 16) for _ in range(16)]
    r[0] = s1 % BitVecVal(256,16)
    r[1] = s1 / BitVecVal(256,16)
    r[8] = s2 % BitVecVal(256,16)
    r[9] = s2 / BitVecVal(256,16)
    return r

solver = Solver()
flag = [BitVec('flag%d' % i, 16) for i in range(16)]
masks = [0xff] * 8 + [0x00] + [0xff] * 7 + [0x00] + [0xff] * 7
masks = [BitVecVal(i, 16) for i in masks]

xmm5 = int2bitvecval(xmm5_results[0])
for i in range(8, 0, -1):
    xmm2 = andps_z3(flag, masks[i:i+16])
    xmm5 = psadbw_z3(xmm5, xmm2)
    expected = int2bitvecval(xmm5_results[9-i])
    for j in range(16):
        solver.add(xmm5[j] == expected[j])

if solver.check() == sat:
    m = solver.model()
    # print(m)
    s = []
    for i in range(16):
        s.append(m[flag[i]].as_long())
    # shuffle back
    s = s[12:16] + s[8:12] + s[0:8]
    strs=""
    for i in s:
        strs+=chr(i)
    print "flag"+strs
else:
    print 'unsat'
