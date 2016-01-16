def GCDandLCM(numA,numB):
    if numA<=numB:
        i=numB
        while (i%numA)!=0 or (i%numB)!=0:
            i=i+1
        GCD=i
        i=numA
        while (numA%i)!=0 or (numB%i)!=0:
            i=i-1
        LCM=i
    elif numA>numB:
        i=numA
        while (i%numA)!=0 or (i%numB)!=0:
            i=i+1
        GCD=i
        i=numB
        while (numA%i)!=0 or (numB%i)!=0:
            i=i-1
        LCM=i
    return GCD,LCM