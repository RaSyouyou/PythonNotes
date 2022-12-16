
a = ['1','2','4','a','b','3.14','嗨嗨嗨','3d3dddd','asd23fasdf','asdfgawegwa',55.32,'dsafasa4242fdsaf',54,'^&*(&)(*','__)*(&*(2323',4,'dfewf',3434]
a_str = [str(i) for i in a ]

a_num = [i for i in a_str ]#if not str.isalpha(i)
print(a_str)
print(a_num)
#print(len(a_num))
#print(len(a_num[4]))
#print(a_num[4])

fuhao = '`~!@#$%^&*()_+|}{":?></.,;[]'




index = []
for i in range(len(a_num)):
    for x in range(len(a_num[i])):
        if str.isalpha(a_num[i][x]) or a_num[i][x] in fuhao:
            index.append(i)
            break

print(index)
strange_requirement= []
for i in range(len(a_num)):
    if i not in index:
        strange_requirement.append(a_num[i])

strange_requirement =[float(i) for i in strange_requirement]
print(strange_requirement)



print(str.isalpha('syntax'))
print(str.isalpha('syntax error'))
print(str.isalpha('dsafasa4242fdsaf'))



