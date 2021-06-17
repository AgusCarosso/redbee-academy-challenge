#SumTwoNumbers: That receives two numbers and returns the sum of both

num1 = int(input("Ingresa el primer numero para sumar: "))
num2 = int(input("Ingresa el segundo numero para sumar: "))

def suma(num1, num2):
    resultado = num1 + num2
    return resultado 

print(suma(num1, num2))

#SumArrayNumbers: That receives a list and return the sum of entire list

list = [1, 5, 8, 22, 34]

def sumList(list):
    res = sum(list)
    return res

print(sumList(list))

#CompareNumbers: That receives three numbers and return the max of them

n1 = int(input("Ingrese el primer numero a comparar: "))
n2 = int(input("Ingrese el segundo numero a comparar: "))
n3 = int(input("Ingrese el tercer numero a comparar: "))

def numMax(n1, n2, n3):
    result = max(n1, n2, n3)
    return result

print(numMax(n1, n2, n3))

#CompareArrayNumbers: That receives two lists of numbers and returns a list with the max of both

list1 = [5, 10, 15, 20]
list2 = [3, 6, 9, 12]

def comparacion(list1, list2):
    compareList = max(list1 + list2)
    return compareList

print(comparacion(list1, list2))