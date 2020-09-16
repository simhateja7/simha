b={}
def most_frequent(a):
    b["i"]=a.count("i")
    b['s']=a.count('s')
    b['p']=a.count('p')
    b['m']=a.count('m')
    return
most_frequent("mississippi")
#print(b)
for k in b:
    print(k,'= 0'+str(b[k]))

