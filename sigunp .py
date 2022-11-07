from calendar import month
import json
import re
import os
print("WELCOME IN LOGIN AND SIGNUP PAGE")
file=os.path.isfile("signup.json")
if file ==False:
    l=[]
    with open("signup.json","a")as h:
        a=json.dump(l,h,indent=2)
user=input("what you want to do login and signup:")
if user=="signup":
    n=input("enter yoru name :")
    n1=input("enter the number :")
    d=open("signup.json","r")
    n2=d.read()
    if n not in n2:
        print("create a strong password with a mixture of letter number and symbols")
        def pas():
            paas=input("enter your paasword :")
            if (re.search(("[a-z A-Z]"),paas) and re.search("[0-9]",paas) and (re.search("[@#$&]",paas))):
                if len(paas)>=8:
                    confirm=input("enter the confirm password :")
                    if paas==confirm:
                        print("correct password :")
                        dob=input("enter your date of birth :")
                        month=input("enter the month :")
                        year=input("enter the year :")
                        g=input("enter your  gender male or femle :")
                        gmail=input("enter yoru own gmail  :")
                        print(n,"your signup is successfully ")
                        dic={"name":n,"password":paas,"dob":dob,"month":month,"year":year,"gender":g,"gmail":gmail}
                        with open("signup.json","r")as z:
                            data=json.load(z)
                        data.append(dic)
                        with open("signup.json","w")as z:
                            json.dump(data,z,indent=2)
                    else:
                        print("password not matched")
                        pas()
                else:
                    print("password must be longer than8 charcter")
                    pas()
            else:
                print("invalid password","password")
        pas()
    else:
        print("name is already exist")
elif user=="login":
    usernme=input("enter your name")
    a1=input("enter the password")
    with open("signup.json","r") as q:
        da=json.load(q)
        for i in range (len(da)):
            if da[i]["name"]==usernme:
               if da[i]["password"]==a1:
                   print("login successfully")
                   print("your name is",da[i]["name"],"\n")
                   print("and your data is :-\n")
                   for x,y in da[i].items():
                    print(x,"=",y)
                    print("you are login suceesfull")
               else:
                   print("incorrect  password")
                   break