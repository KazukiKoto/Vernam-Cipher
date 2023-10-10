def Input():
    plaintext = input(print("Enter Message to encrypt")) #Takes user input for key and message
    key = input(print("Enter key to encrypt with"))
    if len(key) < len(plaintext):
        print("Key cannot be shorter than message")
        Input()
    Conv(plaintext,key)
    
def Conv(plaintext,key):
    PlaintextBinaryArray=[]
    KeyBinaryArray=[]
    for i in range(len(plaintext)):
        PlaintextBinaryArray.append(format(int(ord(plaintext[i])), "b")) #Converts characters to binary
    for i in range(len(key)):
        KeyBinaryArray.append(format(int(ord(key[i])), "b"))
    print("Plaintext in Binary:")
    print(PlaintextBinaryArray)
    print("Key in Binary:")
    print(KeyBinaryArray)
    Vernam(PlaintextBinaryArray,KeyBinaryArray)
    
def Vernam(PlaintextBinaryArray,KeyBinaryArray):
    EncryptedArray=[]
    for i in range(len(PlaintextBinaryArray)):
        a=PlaintextBinaryArray[i]
        b=KeyBinaryArray[i]
        EncryptedArray.append((format(int(a,2)^int(b,2),"b")).zfill(len(a))) #XOR the key and message then fills gaps to make all binary the same length
    print("Encrypted Message:")
    print(EncryptedArray)
    VernamDecipher(EncryptedArray,KeyBinaryArray)
    
def VernamDecipher(EncryptedArray,KeyBinaryArray):
    DecryptedArray=[]
    for i in range(len(EncryptedArray)):
        a=EncryptedArray[i]
        b=KeyBinaryArray[i]
        DecryptedArray.append(int((format(int(a,2)^int(b,2),"b")).zfill(len(a)),2)) #XOR to get original binary back and convert to ASCII
    print("Decrypted Plaintext in ASCII:")
    print(DecryptedArray)
    Deconv(DecryptedArray)

def Deconv(DecryptedArray):
    Plaintext=""
    for i in range(len(DecryptedArray)):
        Plaintext=Plaintext+chr(DecryptedArray[i]) #Convert back into plaintext
    print("Final Message:")
    print(Plaintext)
Input()