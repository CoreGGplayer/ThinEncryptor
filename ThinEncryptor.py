import random
inputer=input("Encrypt Text:")
string_list, byte1, byte2, byte3, byte3_list, random_num_1, random_num_2, temporary_var_1, temporary_var_2, temporary_var_3, byte4, byte5, result_list= ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "[", "}", "]", "|", " ", ":", "", "<", ">", ",", ".", "?", "/", " "], inputer.encode(), "", "", [], 0, 0, 0, 0, 0, "", "", []
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
    byte3_list.append(byte3)
    byte3=""
for i in byte3_list:
    byte4=i.encode()
    for i in byte4:
        temporary_var_3=int(i)
        byte5+=str(temporary_var_3)
    result_list.append(byte5)
    byte5=""
for i in result_list:
    print(i)
