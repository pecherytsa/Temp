from numpy import *
from decimal import getcontext, Decimal
getcontext().prec = 5
n = 4
A = [ [6.81, 1.08, 0.99, 1.165],  # исходная матрица
      [1.08, 3.61, 1.3, 0.16],
      [0.99, 1.3, 5.99, 2.1],
      [1.165, 0.16, 2.1, 5.55] ]



L = [ [double(0) for i in range(n)] for j in range(n) ]   # заполнение матриц нулями
R = [ [double(0) for i in range(n)] for j in range(n) ]

A = reshape(A, (n,n))    # преобразование матриц для удобного вывода
L = reshape(L, (n,n))
R = reshape(R, (n,n))
print("A = ")
print(A)

def setLR():                                          # первый вариант функции
    for i in range(n):
        for j in range(n):
            R[0][i] = A[0][i]
            L[i][0] = A[i][0] / R[0][0]
            sum = 0
            for k in range(i):
                sum += L[i][k] * R[k][j]
            R[i][j] = A[i][j] - sum
            if i > j:
                L[j][i] = 0
            else:
                sum = 0
                for k in range(i):
                    sum += L[j][k] * R[k][i]
                L[j][i] = (A[j][i] - sum) / R[i][i]



   # R[2][0] = 0
    print("L = ")
    print(L)
    print("R = ")
    print(R)

def setLR2():                                         # второй вариант функции
    for j in range(n):
        R[0][j] = A[0][j]
        L[j][0] = A[j][0] / R[0][0]
        L[j][j] = 1

    for i in range(1, n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += L[i][k] * R[k][j]
            R[i][j] = A[i][j] - sum
        for j in range(i + 1, n):
            sum = 0
            for k in range(i):
                sum += L[j][k] * R[k][i]
            L[j][i] = ( A[j][i] - sum ) / R[i][i]
    print("L = ")
    print(L)
    print("R = ")
    print(R)


setLR()        # выполнение алгоритма с помощью первой функции
D = L@R        # матрица D = L*R
print(D)


# в питоне нет круглых скобок { } для вложений
# вместо этого используются отступы:
for i in range(n):
    a = n       # эти две строки
    b = n + 1   # выполняются в теле цикла for
c = n       # а эта выполняется один раз только после окончания цикла







