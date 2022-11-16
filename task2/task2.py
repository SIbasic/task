with open('файл1.txt') as f:
    s1 = f.readline().replace('\n', '').replace('\r', '').replace(' ', '')
    r1 = f.readline(2).replace('\n', '').replace('\r', '').replace(' ', '')
with open('файл2.txt') as f:
    s2 = f.read().replace('\n', '').replace('\r', '').replace(' ', '')

myArr2 = [i for i in s2]

myArr1 = [i for i in s1]

arrXk = myArr1[::2]
arrYk = myArr1[1::2]
arrX = myArr2[::2]
arrY = myArr2[1::2]

for i in range(len(arrX)):
    if (int(arrX[i]) - int(arrXk[0])) ** 2 / int(r1[0]) ** 2 + (int(arrY[i]) - int(arrYk[0])) ** 2 / int(r1[0]) ** 2 < 1:
        print(" 1 ")
    elif (int(arrX[i]) - int(arrXk[0])) ** 2 / int(r1[0]) ** 2 + (int(arrY[i]) - int(arrYk[0])) ** 2 / int(r1[0]) ** 2 == 1:
        print(" 0 ")
    else:
        print(" 2 ")