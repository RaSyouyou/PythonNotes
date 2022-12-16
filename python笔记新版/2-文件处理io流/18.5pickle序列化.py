import pickle

with open(r'data.dat','wb') as f:
    a1 = 'auxiliary mining unit activated'
    a2 = 114514
    a3 = [50,100,'upgrate completed']

    pickle.dump(a1,f)
    pickle.dump(a2,f)
    pickle.dump(a3,f)



with open('data.dat','rb') as f:
    r1 = pickle.load(f)
    r2 = pickle.load(f)
    r3 = pickle.load(f)


    print(r1)
    print(r2)
    print(r3)

print(r1==a1)
print(id(r1)==id(a1))