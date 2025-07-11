def psswrd():
    global password
    password=input("Enter password: ")
    if password=='':
        psswrd()
    elif password!='':
        l=length()
        c=cap()
        s=symbol()
        n=num()
    return password
    
def cap():
    for i in password:
        count_cap=0
        #print(i)
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            count_cap+=1
            break
        else:
            continue
    if count_cap==0:
        print("Your password should have atleast 1 Capital letter")
        psswrd()
    else:
        return True

def symbol():
    for i in password:
        count_sym=0
        if i in '''~!@#$%^&*()`=+,./<>?;':"[]{}|-\_''':
            count_sym+=1
            break
        else:
            continue
    if count_sym==0:
        print("Your password should have atleast 1 special symbol")
        psswrd()
    else:
        return True

def num():
    for i in password:
        count_num=0
        if i in "1234567890":
            count_num+=1
            break
        else:
            continue
    if count_num==0:
        print('Your password should have atleast 1 numeric value')
        psswrd()
    else:
        return True

def length():
    if len(password)<6:
        print('Your password should be greater than 6 character')
        psswrd()
    else:
        return True

def confirm(password):
    password2=input("Confirm Password: ")
    if password==password2:
        print('Password Saved')
        return True
    else:
        print("Password doesn't match")
        return False
        
    

print('''Your password should be greater than 6 character
Your password should have atleast 1 Capital letter
Your password should have atleast 1 special symbol
Your password should have atleast 1 numeric value''')

password=psswrd()
password2=False
while password2==False:
    password2=confirm(password)
