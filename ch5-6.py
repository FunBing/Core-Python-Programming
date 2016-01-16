def operate(formula):
    for i in ["+","-","**","/","%","*"]:
        formula=formula.split(i)
        if len(formula)==2:
            operator=i
            break  
        formula=formula[0]
    numA=float(formula[0])
    numB=float(formula[1])
    if operator=="+":
        return numA+numB
    elif operator=="-":
        return numA-numB
    elif operator=="*":
        return numA*numB
    elif operator=="/":
        return int(numA)/int(numB)
    elif operator=="%":
        return numA%numB
    elif operator=="**":
        return numA**numB
        