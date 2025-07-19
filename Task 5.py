counter = 0  # Global variable

def change_counter():
    global counter
    counter += 1
    return counter

# Call multiple times
print("Counter now:", change_counter())
print("Counter now:", change_counter())
