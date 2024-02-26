import hashlib
m = hashlib.new('sha256')
m.update(b"ini password!")
hdec = m.hexdigest()
print(f"hasil encryptsi :\n{hdec}")