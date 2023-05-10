
    
n = int(input())
d = {5: 11, 12:41, 9:47, 20:61, 12:41}
list = []
for i in range(n):
    a = int(input())
    list.append(a)

def f(x):
    return x * 2 
for i in range(n):
    if list[i] in d:
        print(d[list[i]])
    elif list[i] not in d:
        print(f(list[i]))
        d[list[i]] = f(list[i])

print(f'the input number is:{n}')



    
    
