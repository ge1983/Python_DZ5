### Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def Number(A,B):
     if B == 0:
        return 1
     return A * Number(A, B-1)
     
     
A=int(input("Введите число A: "))
B=int(input("Введите число B: "))
print(Number(A,B))