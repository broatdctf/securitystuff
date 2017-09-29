secret_song = ''
# ---------------------------------------------------------------------
def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)
# ---------------------------------------------------------------------
f = open ("jaksjkljaflk124.dctf.def.camp", "r")
buf =f.read()
f.close()
if __name__ == '__main__':
    key = buf
    encrypted = secret_song
    decrypted = decrypt(key, encrypted)

    print 'Key:', repr(key)
    print 'Decrypted:', repr(decrypted)
