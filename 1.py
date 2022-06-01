number = 1
a = 0
list=[]
while(number != 0):
    number = int(input())
    if(number != 0):
        list.append(number)
        a = a+1
list1 = sorted(list)
print("было ",list)
print("стало",list1)
