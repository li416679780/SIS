from z3 import *

username = [BitVec('u%d'%i,8) for i in range(0,4)]
solver = Solver() #76876-77776
solver.add(((username[0]&1)+5+(((username[1]>>2) & 1 )+1))==ord('7')-0x30)
solver.add(((((username[0]>>3) & 1)+5)+(((username[1]>>3)&1)+1))==ord('6')-0x30)
solver.add((((username[0]>>1) & 1)+5+(((username[1]>>4) & 1 )+1))==ord('8')-0x30)
solver.add((((username[0]>>2) & 1)+5+(((username[1]) & 1 )+1))==ord('7')-0x30)
solver.add((((username[0]>>4) & 1)+5+(((username[1]>>1) & 1 )+1))==ord('6')-0x30)
solver.add((((username[2]) & 1)+5+(((username[3]>>2) & 1 )+1))==ord('7')-0x30)
solver.add((((username[2]>>3) & 1)+5+(((username[3]>>3) & 1 )+1))==ord('7')-0x30)
solver.add((((username[2]>>1) & 1)+5+(((username[3]>>4) & 1 )+1))==ord('7')-0x30)
solver.add((((username[2]>>2) & 1)+5+(((username[3]) & 1 )+1))==ord('7')-0x30)
solver.add((((username[2]>>4) & 1)+5+(((username[3]>>1) & 1 )+1))==ord('6')-0x30)
solver.add(username[3] == ord('p'))
for i in range(0,4):
    solver.add(username[i] >= ord('a'))
    solver.add(username[i] <= ord('z'))

solver.check()
result = solver.model()

flag = ''
for i in range(0,4):
    flag += chr(result[username[i]].as_long().real)
print flag
