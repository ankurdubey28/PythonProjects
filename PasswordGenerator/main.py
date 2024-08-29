import random
import string
map={
    "yes":True,
    "no":False
}
def generate_password(min_len,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    pwd=""

    candidates=list(letters)
    if numbers==True:
        candidates+=digits
    if special_characters==True:
        candidates+=special

    for _ in range(min_len):
        chosen=random.choice(candidates)
        pwd+=chosen

    return pwd



min_len=input("Enter Password length: ")
has_numbers=input("Should password contain numbers? (Yes/NO) :")
has_characters=input("Should password contain characters? (Yes/No) : ")
if min_len.isdigit()!=True or isinstance(has_numbers,str)!=True or isinstance(has_characters,str)!=True:
    print("Enter valid Inputs")
else:
    print(generate_password(int(min_len),map[has_numbers.lower()],map[has_characters.lower()]))