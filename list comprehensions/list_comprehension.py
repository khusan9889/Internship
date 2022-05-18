#Example of problem solution with simple lists
'''square of numbers from 1-100'''

print("squares\n")
squares = []
for i in range(1,101):
    squares.append(i**2)
print(squares)

#Here is solution example with LIST COMPREHENSION
squares2 = [i**2 for i in range(1,101)]
print(squares2,)


#Преобраззование вводимых строчных цифрт в консоли через пробел в int тип данных
print("Convert list into int dt\n")
a = input().split()
a = [int(i) for i in a]
print(a)


#2D array with list comprehension
print("2Dimentional array with LIST COMPREHENSION\n")
n = 5
m = 4

a = [[0]*m for i in range(n)]
a[1][3] = 100 #change element in [1][3] position
for i in a:
    print(i)

#2loops
print("2LOOPS\n")
a = [(i,j) for i in 'abc' for j in (1,2,3)]
print(a)

