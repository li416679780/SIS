def encrypt ( v, k):  
    v0=v[0], v1=v[1], sum=0, i;           /* set up */  
    delta=0x9e3779b9;                     /* a key schedule constant */  
    k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */  
    for i in xrange(0,32):                       /* basic cycle start */  
        sum += delta;  
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);  
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);  
                                               /* end cycle */  
    v[0]=v0; v[1]=v1;  

def decrypt ( v,  k):  
    v0=v[0], v1=v[1], sum=0xC6EF3720, i;  /* set up */  
    delta=0x9e3779b9;                     /* a key schedule constant */  
    k0=k[0], k1=k[1], k2=k[2], k3=k[3];   /* cache key */  
    for i in xrange(0,32):                         /* basic cycle start */  
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);  
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);  
        sum -= delta;  
                                                  /* end cycle */  
    v[0]=v0; v[1]=v1;  
#xtea
def encipher(num_rounds, v, key) {  
     v0=v[0], v1=v[1], sum=0, delta=0x9E3779B9;  
    for i in xrange(0,num_rounds):  
        v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);  
        sum += delta;  
        v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);  
      
    v[0]=v0; v[1]=v1;  
  
def decipher(num_rounds, v,  key) {   
    v0=v[0], v1=v[1], delta=0x9E3779B9, sum=delta*num_rounds;  
    for i in xrange(0,num_rounds):  
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);  
        sum -= delta;  
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);  
      
    v[0]=v0; v[1]=v1;  
#xxtea
def btea(v, n, key):
    if (n > 1):            /* Coding Part */  
        rounds = 6 + 52/n;  
        sum = 0;  
        z = v[n-1];  
        do
	{ 
            sum += DELTA;  
            e = (sum >> 2) & 3;  
            for (p=0; p<n-1; p++)  
            {  
                y = v[p+1];  
                z = v[p] += MX;  
            }  
            y = v[0];  
            z = v[n-1] += MX;  
        }  
        while (--rounds);  
    }  
    elif (n < -1):      /* Decoding Part */  
    {  
        n = -n;  
        rounds = 6 + 52/n;  
        sum = rounds*DELTA;  
        y = v[0];  
        do  
        {  
            e = (sum >> 2) & 3;  
            for (p=n-1; p>0; p--)  
            {  
                z = v[p-1];  
                y = v[p] -= MX;  
            }  
            z = v[n-1];  
            y = v[0] -= MX;  
            sum -= DELTA;  
        }  
        while (--rounds);  
    }  


