def evens(n):
    result=[]
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result

n = int(input("Enter a number: "))
k=evens(n)
print(k)