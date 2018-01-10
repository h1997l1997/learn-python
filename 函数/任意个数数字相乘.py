def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

sum=calc([1,2,3,4,5,6,7])
print(sum)
