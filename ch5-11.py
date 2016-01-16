def Even():
    evenNum=[]
    for i in range(21):
        if i%2==0:
            evenNum.append(i)
    return evenNum

def Odd():
    oddNum=[]
    for i in range(21):
        if i%2!=0:
            oddNum.append(i)
    return oddNum
    
def Divided(a,b):
    if a%b==0:
        return True
    else:
        return False