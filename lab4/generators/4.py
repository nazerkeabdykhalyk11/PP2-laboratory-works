def squares(a, b):
    result = []
    for i in range(a, b+1):
        k=i**2
        result.append(k)
    return result

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
k=squares(a, b)
print(k)