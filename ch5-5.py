def turnToChange(money):
    money=money*100
    numOf25=numOf10=numOf5=numOf1=0
    if money>25:
        numOf25=money//25   
        money=money%25
    if money>10:
        numOf10=money//10
        money=money%10
    if money>5:
        numOf5=money//5
        money=money%5
    numOf1=money
    return numOf25,numOf10,numOf5,numOf1