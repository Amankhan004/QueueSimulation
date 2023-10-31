import math
import random
from tabulate import tabulate
# Lambda = 2.25
# mew = 8.98
# A = 55
# M = 1994
# Z0 = 10112166
# C = 9
# a = 1
# b = 3


def poissonPDF(x, arrivalRate):
    return (math.exp(-arrivalRate)*(arrivalRate**x)) / (math.factorial(x))

def cumulative_pdf_distro(arrivalRate, serviceRate, a, b, c, seed, A, m):
    result = []
    arrivalTime = []
    serviceTime = []
    R = []
    Z = []
    randomNumber = []
    priorities = []

    # Formulae
    #R = (A*Zi+c)Mod m
    #Y= (b-a)*xi + a
    #random number = R/m

    x = 0
    arrival = 0
    cumulativeProbability = 0

    while(cumulativeProbability <= 0.9999):
        probability = poissonPDF(x, arrivalRate)
        cumulativeProbability += probability
        interArrivalTime = math.ceil(random.randint(0, 6))
        arrival += interArrivalTime
        service = math.ceil((serviceRate) * math.log(random.randint(1, 10)))
        serviceTime.append(service)
        arrivalTime.append(arrival)
        Z.append(seed)
        rValue = (A*seed+c)%m
        R.append(rValue)
        seed = rValue
        rnNumber = rValue/m
        randomNumber.append(rnNumber)
        priority = round((b - a) * rnNumber  + a)
        priorities.append(priority)


        result.append([arrivalTime[x], serviceTime[x], Z[x], R[x], randomNumber[x], priorities[x]])
        x+=1

    table = tabulate(result, headers=["Arrival Time", "Service Time", "ZValue", "R Value", "Random Number", "Priority"])
    print(table)
    return x-1, cumulativeProbability


if __name__ == "__main__":
    serviceRate = float(input("Give service mean for the distribution: "))
    arrivalRate = float(input("Give arrival mean for the distribution: "))
    A = float(input("Give the value for A: "))
    a = float(input("give the value for a: "))
    b = float(input("Give the value for b: "))
    c = float(input("Give value for c: "))
    m = float(input("Give the value for M: "))
    seed = float(input("Give the value for Z: "))

    x, cumulativeProbability = cumulative_pdf_distro(arrivalRate, serviceRate, a, b, c, seed, A, m)

    print(f"Total customers handled: {x}")
    print(f"Cumulative Probability threshold: {round(cumulativeProbability)}")
