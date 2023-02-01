import hashlib


def dehash():

    hashed_msg = str(input("Enter your Hash : "))
    
    f = open(r'E:\Python Security\Hachlib\wordlist.txt' , 'r')

    for line in f:

        text =line.strip() # to remove any space 

        encoded_text = hashlib.md5(text.encode())

        gen_hash  =encoded_text.hexdigest()

        if gen_hash == hashed_msg:

            print(f"[+] your msg is ==> {text}")

    f.close()


dehash()

