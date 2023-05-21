import random
a=input("Lock Text:")
add_list=["~","`","!","@","#","$","%","^","&","*","(",")","{","[","}","]","|"," ",":","'","<",">",",",".","?","/"]
byte1=a.encode('utf-8')
byte2=""
byte3=""
rdi=0
rdi2=0
r=0
r2=0
for i in byte1:
    try:
        r=int(i)
    except ValueError:
        byte2+=i
    byte2+=str(r)
for i in byte2:
    byte3+=i
    rdi=random.randint(0,8)
    for i in range(rdi):
        rdi2=random.randint(0,25)
        byte3+=add_list[rdi2]
print(byte3)