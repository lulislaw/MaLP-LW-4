menz = []
bolz = []
avg = 0
arr = []

number = input()
while number != "":
    num = int(number)
    arr.append(num)
    number = input()
avg = sum(arr) / len(arr)
print("AVG =", avg)
for i in range(len(arr)):
    if(arr[i] < avg):
        menz.append(arr[i])
for i in range(len(arr)):
    if(arr[i] > avg):
        bolz.append(arr[i])
print("< avg:", menz)
print("> avg:", bolz)