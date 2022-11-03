import hashlib
user =  "ashrafuzzaman.shovon.786@gmail.com"
pwd = "diskalaktingbokibat"

pas_encode = pwd.encode()
pas_hash = hashlib.md5(pas_encode).hexdigest()
print(pas_hash)
