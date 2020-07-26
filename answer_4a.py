def prime(n):
    ls = [2,3]
    if (n < 3):
        return ls[:n]
    for i in range(2,n):
        generate = ls[-1]+2
        while any(not(generate%num) for num in ls):
            generate += 2
        ls.append(generate)
    return ls



n = int(input("Enter the number of prime numbers to be displayed:"))
print (prime(n))
