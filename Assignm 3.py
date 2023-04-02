n1=int(input("Enter a number"))
if n1 % 3 ==0 and n1 % 5 == 0:
    print("FizzBuzz")
elif n1 % 3 == 0:
    print("Fizz")
elif n1 % 5 == 0:
    print("Buzz")
elif n1 % 3 != 0 and n1 % 5 != 0:
    print(n1)
