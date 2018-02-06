### The program will ask the input and it will be output the fabnacci series upto the number which will be provided
### Python version - 3.6.2

number=int(input())

a,b=0,1

while b < number:
    a,b=b,a+b
    print(b,end=' ')
