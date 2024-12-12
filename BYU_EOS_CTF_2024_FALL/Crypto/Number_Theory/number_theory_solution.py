from Crypto.Util.number import long_to_bytes, bytes_to_long
import math
import random

'''
pip install pycryptodome
'''

# Values from out.txt
ciphertext = 0xaaa53dd882f6fca0c4a3860863920aa5e97b44dedd3373ed5f102ad4fbb3421c
field = 0xc16a46fd8075947f252507b8021077fbdb6af1cc0f717988c659d1159c09678f
mask = 0x27a8d0a955b3e82d29b57ea33a941949

# Unmask the ciphertext
unmasked = ciphertext ^ mask

def find_flag(unmasked, field):
    # We know 0x1337 + k is the exponent, and k is between 1 and 2^5
    for k in range(1, 2**5 + 1):
        exponent = 0x1337 + k
        
        # Ensure the extra condition in the original script
        if math.gcd(exponent, field-1) != 1:
            continue
        
        try:
            # Compute the modular logarithm (discrete logarithm)
            flag_as_int = pow(unmasked, pow(exponent, -1, field-1), field)
            
            # Convert to bytes
            flag_bytes = long_to_bytes(flag_as_int)
            
            # Check if the flag looks reasonable
            if all(32 <= b <= 126 for b in flag_bytes):
                return flag_bytes
        except Exception as e:
            print(f"Error with k={k}: {e}")
            continue
    
    return None

result = find_flag(unmasked, field)
print(result)