def Payment(openBalance,monthlyPayment):
    print "    Amount Remaing"
    print "Pymt#\tPaid\tBalance"
    print "-----\t-----\t-------"
    pymt=0
    paid=0
    balance=openBalance
    while balance>=0:
        print "%d\t$%.2f\t$%.2f"%(pymt,paid,balance)
        #end flag
        if balance==0:
            balance=-1
        elif balance>monthlyPayment:
            paid=monthlyPayment
            balance=balance-monthlyPayment
        else:
            paid=balance
            balance=0
        pymt=pymt+1      
        
        
if __name__=="__main__":
    openBalance=float(raw_input("Enter opening balance: "))
    monthlyPayment=float(raw_input("Enter monthly payment: "))
    Payment(openBalance,monthlyPayment)