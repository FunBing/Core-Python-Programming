a=float(raw_input())
b=float(raw_input())
c=float(raw_input())
if(a>b):
    a,b=b,a
if(a>c):
    a,b,c=c,a,b
else:
    if(b>c):
        b,c=c,b
print a,b,c
a=float(raw_input())
b=float(raw_input())
c=float(raw_input())
if(a<b):
    a,b=b,a
if(a<c):
    a,b,c=c,a,b
else:
    if(b<c):
        b,c=c,b
print a,b,c
    

    