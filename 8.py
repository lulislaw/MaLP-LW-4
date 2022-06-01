arrx = []
arry = []
xi = 0
yi = 0
m = 0
b = 0
xi = input("Ввод x(enter закончить): ")
while xi != "":
    num = float(xi)
    arrx.append(num)
    yi = float(input("Ввод y(float only): "))
    arry.append(yi)
    xi = input("Ввод x(enter закончить): ")
sumxy = float(0)
x2 = 0
sx = sum(arrx)
sy = sum(arry)
avgx = sum(arrx)/len(arrx)
avgy = sum(arry)/len(arry)
xx2 = sum(arrx)**2
n = len(arrx)
for i in range(len(arrx)):
    sumxy = sumxy + (arrx[i] *arry[i])
    x2 = x2 + arrx[i]**2
sumxy = round(sumxy,1)
x2 = round(x2, 1)
m = round((sumxy - ((sx*sy)/n))/(x2-(xx2/n)), 2)
b = round(avgy - m*avgx, 2)

if b >= 0:
    print("y = " ,m ,"* x +" ,b)
else:
    print("y = " , m , "* x" , b)





