def removemm(arra):
    arra.remove(max(arra))
    arra.remove(min(arra))
    return arra
number = 1
a = 0
list=[]
while(number != 0):
    number = int(input())
    if(number != 0):
        list.append(number)
        a = a+1
print(removemm(list))