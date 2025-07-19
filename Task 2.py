def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

#get number from user
num = int(input("Enter a number: "))
print(f"The number is {is_even_or_odd(num)}")
