filename=raw_input('Enter file name: ')
fobj=open(filename,'r')
for eachline in fobj:
    print eachline,
fobj.close()
