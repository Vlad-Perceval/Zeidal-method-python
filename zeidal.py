from multiprocessing.sharedctypes import Value
from pickle import TRUE
from tokenize import Double
import numpy



n = int(input('введите размерность матрицы'))
input_massiv_a = numpy.zeros((n,n))
input_massiv_b = numpy.zeros((n))
input_massiv_answer = numpy.zeros((n))
input_massiv_copya = numpy.zeros((n,n))
input_massiv_copyb = numpy.zeros((n))

max = 0
eps = 0.00001
value = 0

Filename = str('setst1.txt')
def MatrixReader(Filename):
    Filename = open(Filename, "r")
    for i in range(n):
        s = Filename.readline()
        spli = s.split(" ")
        for  j in range (n):
            input_massiv_copya [i,j] = numpy.double(spli[j])
           
           
           
        input_massiv_copyb[i] = numpy.double(spli[n])
    for i in range(n):
        s = Filename.readline()
        spli = s.split(" ")
        for  j in range (n):
            input_massiv_a[i,j] = numpy.double(spli[j])
           
           
        input_massiv_b[i] = numpy.double(spli[n])

   
    Filename.close

def Zeidal(value,max):#сам метод
    for i in range(n):
        input_massiv_answer [i] = input_massiv_b[i]
    print('№\tx1\t\tx2\t\tx3')
    while TRUE:
        print(value, end='')
        for i in range(n):
            print('\t', format(round( input_massiv_answer[i],6),".6f"), end=" ")
        print("")
        for i in range(n):
            max = 0
            r = input_massiv_b[i]
            for j in range(n):
                c = input_massiv_a[i,j] * input_massiv_answer[j]
                r = r+c
            buf = abs(r - input_massiv_answer[i]) #мето рунге
            if (max < buf):
                max = buf
            input_massiv_answer[i] = round(r,7)
        value = value +1
        if(max < eps):
            break
    print('всего итераций',value)
    for i in range(n):
        print('X',i+1, '=', input_massiv_answer[i])

def proverca():# проверка ответа
    for i in range(n):
        sum= numpy.double(0)
        for j in range(n):
            sum = sum + input_massiv_copya[i,j] * input_massiv_answer[j]
        sum = round(sum,2)
        print(sum, '=', input_massiv_copyb[i])
    print(' ')

if __name__ == "__main__":

    MatrixReader(Filename)
    print('Исходная матрица')
    print(input_massiv_a)
    print('массив свободных членов')
    print(input_massiv_b)
    Zeidal(value,max)
    proverca()
