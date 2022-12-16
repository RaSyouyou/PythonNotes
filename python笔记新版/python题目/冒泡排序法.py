import random


list_in = []
for i in range(random.randint(4,10)):
    list_in.append(random.randint(1,100))

print(list_in)
for i in range(1, len(list_in)):
        for j in range(0, len(list_in) - i):
            if list_in[j] > list_in[j + 1]:
                list_in[j], list_in[j + 1] = list_in[j +1], list_in[j]

print(list_in)