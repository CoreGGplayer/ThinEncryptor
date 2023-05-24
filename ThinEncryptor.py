import random
inputer=input("Encryptor Text:")
string_list,byte1,byte2,byte3,result_list,random_num_1,random_num_2,temporary_var_1,temporary_var_2=["~","`","!","@","#","$","%","^","&","*","(",")","{","[","}","]","|"," ",":","","<",">",",",".","?","/"," "],inputer.encode(),"","",[],0,0,0,0
for i in byte1:
    temporary_var_1=int(i)
    byte2+=str(temporary_var_1)
for i in range(len(byte2)):
    for j in byte2:
        random_num_1=random.randint(0,len(byte2))
        for k in range(random_num_1):
            random_num_2=random.randint(0,25)
            byte3+=string_list[random_num_2]
        byte3+=str(j)
    result_list.append(byte3)
    byte3=""
for i in result_list:
    print(i)
