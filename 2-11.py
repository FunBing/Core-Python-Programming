a=[0,0,0,0,0]
print "Please enter five numbers\n"
for i in range(5):
    a[i]=float(raw_input())
choice='0'
choice=raw_input("Please make a choice\n(1)Sum of the five numbers\n(2)Average of the five numbers\n(x)Exit\n")
while(choice!='x'):
    while(choice!='1' and choice!='2' and choice!='x'):
        print choice
        choice=raw_input("Wrong Input\nPlease make a choice\n(1)Sum of the five numbers\n(2)Average of the five numbers\n(x)Exit\n")
    if choice=='1':
        sum_of_num=0
        for i in range(5):
            sum_of_num+=a[i]
        print sum_of_num
    elif choice=='2':
        average_of_num=0
        for i in range(5):
            average_of_num+=a[i]
        average_of_num/=5
        print average_of_num
    else:
        break
    print "Do it again!\nPlease enter five numbers\n"
    for i in range(5):
        a[i]=float(raw_input())
    choice=raw_input("Please make a choice\n(1)Sum of the five numbers\n(2)Average of the five numbers\n(x)Exit\n")
                
