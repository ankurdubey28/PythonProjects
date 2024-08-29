from cryptography.fernet import Fernet
def Load_Key():
    return open("key.key",'rb').read()


pwd=input("Enter Master Password:")
key=Load_Key()+pwd.encode()
fer=Fernet(key)

# def Write_Key():
#     key=Fernet.generate_key()
#     with open("key.key","wb")as keyfile:
#         keyfile.write(key)
#
# Write_Key()



def View():
    with open("PWD.txt", 'r') as f:
        for word in f.readlines():
            usernanme,password=word.rstrip().split("|")
            print("Username: "+usernanme+","+"Password: "+fer.decrypt(password).decode())

def Add():
    name=input("Account name: ")
    password=input("Password: ")

    with open("PWD.txt", 'a') as f:
        f.write(name+ "|" +fer.encrypt(password.encode()).decode() +"\n")

while(True):
    mode=input("View Password or Add Password (view , add) or Press Q to quit:").lower()
    if mode=="view":
        View()
    elif mode=="add":
        Add()
    elif mode=="q":
        break
    else:
        print("Invalid mode")
        continue