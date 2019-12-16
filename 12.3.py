import random
import math

def RingS(R1,R2):
    return math.pi * (R1 ** 2 - R2 ** 2)

def CircleS(R):
    return math.pi * R ** 2


for i in range(0, 3):
    print(i)
    L = input("L = ")
    print("R_1 = {0}; R_2 = {1}".format(L[0], L[1]))
    print("Площадь круга 1: ", CircleS(L[0]))
    print("Площадь круга 2: ", CircleS(L[1]))
    print("Площадь кольца: ", RingS(L[0], L[1]))