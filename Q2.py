from math import factorial as fct, log, e

def higher(l):
    h=l[0]
    for j in range(len(l)):
        if l[j]>h:
            h=l[j]
        else:
            continue
    return h

list=[]
for i in range(10):
    if i%2==0:
        list.append(3**i + 7*fct(i))
    else:
        list.append(2**i+4*log(i, e))
print(list)
print(sum(list)/len(list), higher(list))
