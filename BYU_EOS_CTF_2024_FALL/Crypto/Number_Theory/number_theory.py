from Crypto.Util.number import bytes_to_long, getPrime
import random, math

flag = b"REDACTED"
field = getPrime(256)
mask = random.randint(1, 2**128)
assert len(bin(field)) > len(bin(bytes_to_long(flag))), "Field is too small"

while True:
    k = random.randint(1, 2**5)
    if math.gcd(0x1337+k,field-1) != 1:
        # bonus points if you can tell me why this is here
        continue
    print("Ciphertext =", hex(((bytes_to_long(flag) ** (0x1337+k)) % field)^mask))
    print("Field = F(", hex(field), ")")
    print("Mask = ", hex(mask))
    break