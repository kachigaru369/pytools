key = 0x42

def xor_decrypt(char):
    return chr(ord(char) ^ key)

with open("/tmp/.keylog.txt", "r") as f:
    encrypted = f.read()

decrypted = "".join([xor_decrypt(c) for c in encrypted])
print("Decrypted log:\n", decrypted)


# chr(ord(char) ^ key)