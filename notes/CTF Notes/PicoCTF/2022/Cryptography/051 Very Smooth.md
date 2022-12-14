#pico2022 #cryptography 

## Challenge:
```md
Forget safe primes... Here, we like to live life dangerously... >:)

-   [gen.py](https://artifacts.picoctf.net/c/131/gen.py)
-   [output.txt](https://artifacts.picoctf.net/c/131/output.txt)
```

## Process:
Download the files.
```bash
curl -O https://artifacts.picoctf.net/c/131/gen.py
curl -O https://artifacts.picoctf.net/c/131/output.txt
```
#curl 

The hint recommends looking at *Pollard*. I found [this pdf](http://www.math.columbia.edu/~goldfeld/PollardAttack.pdf).

Looking at the *output.txt*
```bash
cat output.txt
```

```
n = 6df1b3e09c344f8cf16c6fd9bdcc140e7c7c44c1ffd9c8439aa28599bf4f5691ab107314d51194dff5b3b6dcfd84d03e8067eee1bc2554f10ecae55beb6b4f7406b1a76790e30f1a5688edf773f0dfb65477270054fedf94f21bfabaa5781200974a5c7fa1c863fccf8689a8a13302d1a861f82c678604a73400b4ab1532eec5472c56720fbe336e24a7e855a5b46a8a7b64224c8be263fef1c8eb263f6e6690a41648077aa6629956f719bb4150e411d6d1e04d61347710596f988d91dcf306e44688f1919f860c56508d1079f994cd45e0d8305ea1d2211d1579a2c90e6bf155672a4d893e981f579b4942af50ed2ce18bcb3625b16a4cf9d2b7cf195f1f85
c = 527d16b8a5e8a99a8138331b94ef1f8bed77fcdc27c4a664ef7495b72ea90a26c9a17e3d62db612fb8176a9ae8687f8c16b43c0fe279837b8e63aac96b8b170aa5e24a852c1ae60bb948e15c60155672ac6c8d0d789e4bb186102c4b8aebf1b88acb250da8ed7c6dc244c44b8ec458ca55d09884ab8db3bbc544e3cacab7a6eb8fbe6c267cc496317a4fbe6dbb32681211c1ffb0b5da4e84035306ff4abd7c53e5f6247073bbf5d656a2d700263bee67c43d1c8c842e631fde93aefae78b09bd62239620b80e0caa0d43b5e7a779bbaae669b14d9da819f1707619e12604c92641a64519275a8ba824d4c90e088708b59cb8ee8ce3729e1f3b6eb6359cb706ad
```

And looking at the *python* file.
```python
#!/usr/bin/python

from binascii import hexlify
from gmpy2 import *
import math
import os
import sys

if sys.version_info < (3, 9):
    math.gcd = gcd
    math.lcm = lcm

_DEBUG = False

FLAG  = open('flag.txt').read().strip()
FLAG  = mpz(hexlify(FLAG.encode()), 16)
SEED  = mpz(hexlify(os.urandom(32)).decode(), 16)
STATE = random_state(SEED)

def get_prime(state, bits):
    return next_prime(mpz_urandomb(state, bits) | (1 << (bits - 1)))

def get_smooth_prime(state, bits, smoothness=16):
    p = mpz(2)
    p_factors = [p]
    while p.bit_length() < bits - 2 * smoothness:
        factor = get_prime(state, smoothness)
        p_factors.append(factor)
        p *= factor

    bitcnt = (bits - p.bit_length()) // 2

    while True:
        prime1 = get_prime(state, bitcnt)
        prime2 = get_prime(state, bitcnt)
        tmpp = p * prime1 * prime2
        if tmpp.bit_length() < bits:
            bitcnt += 1
            continue
        if tmpp.bit_length() > bits:
            bitcnt -= 1
            continue
        if is_prime(tmpp + 1):
            p_factors.append(prime1)
            p_factors.append(prime2)
            p = tmpp + 1
            break

    p_factors.sort()

    return (p, p_factors)

e = 0x10001

while True:
    p, p_factors = get_smooth_prime(STATE, 1024, 16)
    if len(p_factors) != len(set(p_factors)):
        continue
    # Smoothness should be different or some might encounter issues.
    q, q_factors = get_smooth_prime(STATE, 1024, 17)
    if len(q_factors) != len(set(q_factors)):
        continue
    factors = p_factors + q_factors
    if e not in factors:
        break

if _DEBUG:
    import sys
    sys.stderr.write(f'p = {p.digits(16)}\n\n')
    sys.stderr.write(f'p_factors = [\n')
    for factor in p_factors:
        sys.stderr.write(f'    {factor.digits(16)},\n')
    sys.stderr.write(f']\n\n')

    sys.stderr.write(f'q = {q.digits(16)}\n\n')
    sys.stderr.write(f'q_factors = [\n')
    for factor in q_factors:
        sys.stderr.write(f'    {factor.digits(16)},\n')
    sys.stderr.write(f']\n\n')

n = p * q

m = math.lcm(p - 1, q - 1)
d = pow(e, -1, m)

c = pow(FLAG, e, n)

print(f'n = {n.digits(16)}')
print(f'c = {c.digits(16)}')

```
#python 

Here we find *e*.
```python
e = 0x10001
```

Now to use the tool [*RsaCtfTool*](https://github.com/RsaCtfTool/RsaCtfTool).
```bash
cd ~/tools/RsaCtfTool
```

```bash
python RsaCtfTool.py -n 0x6df1b3e09c344f8cf16c6fd9bdcc140e7c7c44c1ffd9c8439aa28599bf4f5691ab107314d51194dff5b3b6dcfd84d03e8067eee1bc2554f10ecae55beb6b4f7406b1a76790e30f1a5688edf773f0dfb65477270054fedf94f21bfabaa5781200974a5c7fa1c863fccf8689a8a13302d1a861f82c678604a73400b4ab1532eec5472c56720fbe336e24a7e855a5b46a8a7b64224c8be263fef1c8eb263f6e6690a41648077aa6629956f719bb4150e411d6d1e04d61347710596f988d91dcf306e44688f1919f860c56508d1079f994cd45e0d8305ea1d2211d1579a2c90e6bf155672a4d893e981f579b4942af50ed2ce18bcb3625b16a4cf9d2b7cf195f1f85 --uncipher 0x527d16b8a5e8a99a8138331b94ef1f8bed77fcdc27c4a664ef7495b72ea90a26c9a17e3d62db612fb8176a9ae8687f8c16b43c0fe279837b8e63aac96b8b170aa5e24a852c1ae60bb948e15c60155672ac6c8d0d789e4bb186102c4b8aebf1b88acb250da8ed7c6dc244c44b8ec458ca55d09884ab8db3bbc544e3cacab7a6eb8fbe6c267cc496317a4fbe6dbb32681211c1ffb0b5da4e84035306ff4abd7c53e5f6247073bbf5d656a2d700263bee67c43d1c8c842e631fde93aefae78b09bd62239620b80e0caa0d43b5e7a779bbaae669b14d9da819f1707619e12604c92641a64519275a8ba824d4c90e088708b59cb8ee8ce3729e1f3b6eb6359cb706ad -e 0x1001
```

This tool was currently broken, so let's do some scripting. 
```python
#!/usr/bin/env python3

from Crypto.Util.number import *
from math import gcd

n = 0x6df1b3e09c344f8cf16c6fd9bdcc140e7c7c44c1ffd9c8439aa28599bf4f5691ab107314d51194dff5b3b6dcfd84d03e8067eee1bc2554f10ecae55beb6b4f7406b1a76790e30f1a5688edf773f0dfb65477270054fedf94f21bfabaa5781200974a5c7fa1c863fccf8689a8a13302d1a861f82c678604a73400b4ab1532eec5472c56720fbe336e24a7e855a5b46a8a7b64224c8be263fef1c8eb263f6e6690a41648077aa6629956f719bb4150e411d6d1e04d61347710596f988d91dcf306e44688f1919f860c56508d1079f994cd45e0d8305ea1d2211d1579a2c90e6bf155672a4d893e981f579b4942af50ed2ce18bcb3625b16a4cf9d2b7cf195f1f85
c = 0x527d16b8a5e8a99a8138331b94ef1f8bed77fcdc27c4a664ef7495b72ea90a26c9a17e3d62db612fb8176a9ae8687f8c16b43c0fe279837b8e63aac96b8b170aa5e24a852c1ae60bb948e15c60155672ac6c8d0d789e4bb186102c4b8aebf1b88acb250da8ed7c6dc244c44b8ec458ca55d09884ab8db3bbc544e3cacab7a6eb8fbe6c267cc496317a4fbe6dbb32681211c1ffb0b5da4e84035306ff4abd7c53e5f6247073bbf5d656a2d700263bee67c43d1c8c842e631fde93aefae78b09bd62239620b80e0caa0d43b5e7a779bbaae669b14d9da819f1707619e12604c92641a64519275a8ba824d4c90e088708b59cb8ee8ce3729e1f3b6eb6359cb706ad
e = 0x10001


def pollard(n):
    a = 2
    b = 2

    while True:
        a = pow(a, b, n)
        g = gcd(a-1, n)
        if 1 < g < n:
            return g
        else:
            b += 1

p = pollard(n)
q = n // p

phi = 1
for i in [p, q]:
    phi *= (i-1)

d = inverse(e, phi)
m = pow(c, d, n)

flag = long_to_bytes(m).decode('utf-8')
print(flag)
```
#python 

Outputting:
```
picoCTF{p0ll4rd_f4ct0r1z4at10n_FTW_148cbc0f}
```

Save the flag.
```bash
python getflag.py > flag.txt
```
#python 

**Flag: *picoCTF{p0ll4rd_f4ct0r1z4at10n_FTW_148cbc0f}***
