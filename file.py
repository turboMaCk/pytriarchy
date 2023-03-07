import os
import base64

print(os.getlogin())
encoded = base64.b64encode("os.getlogin()".encode("utf-8"))

print("=> will evaluate:")
print("=>", encoded)
print(eval(base64.b64decode(encoded)))

print("But I can get PATH from env", os.getenv("PATH"))


