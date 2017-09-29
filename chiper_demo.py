def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

if __name__ == '__main__':
    key = 'thispasswordissecret'
    msg = 'I have always believed the you can recover this basic flag from my so basic encryption. And actually you found it in your own way. I appreciate that. Well My friend this is your key: >>>>>>>>> This is a big secret <<<<<<<<<<<<. Now I will just sing a song in order to prelong the length of this message. A B C D E F G Come and sing along with me H I J K L M N O P Tell me what you want to be Q R S T U V W X Y and ZNow I know my ABCs Next time won t you sing with me A B C D E F G H I J K L M N O P Q R S T U V W X Y and Z Now I know my ABCs Next time won t you sing with me! ONE MORE TIME! A B C D E F G Come and sing along with me H I J K L M N O P Tell me what you want to be Q R S T U V W X Y and ZNow I know my ABCs Next time won t you sing with me A B C D E F G H I J K L M N O P Q R S T U V W X Y and Z Now I know my ABCs Next time won t you sing with me!'
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)

    print 'Message:', repr(msg)
    print 'Key:', repr(key)
    print 'Encrypted:', repr(encrypted)
    print 'Decrypted:', repr(decrypted)
