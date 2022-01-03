import bcrypt

salt = bcrypt.gensalt()
mypw = bcrypt.hashpw(b"OskarSchindler", salt)
print(str(mypw), type(str(mypw)))
