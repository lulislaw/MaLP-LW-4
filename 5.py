otric = []
poloz = []
nulle = []

arr = []

number = input()
while number != "":
    num = int(number)
    arr.append(num)
    number = input()

for i in range(len(arr)):
    if(arr[i] < 0):
        otric.append(arr[i])
for i in range(len(arr)):
    if(arr[i] == 0):
        nulle.append(arr[i])
for i in range(len(arr)):
    if(arr[i] > 0):
        poloz.append(arr[i])
print(otric,nulle,poloz)