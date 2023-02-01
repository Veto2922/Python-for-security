import hashlib 

# print(hashlib.algorithms_available)  # to get types of hash

text = "what?"

encoded_txt = hashlib.md5(text.encode()) # sha1 is a one of hashing algorithms

print(encoded_txt.hexdigest())  #  hexdigest يعني اظهر الهاش 