def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

# Get input from user
user_input = input("Enter numbers separated by commas (e.g. 2,3,4): ")
numbers = [int(num.strip()) for num in user_input.split(",")]

print("Squares:", square_numbers(numbers))
