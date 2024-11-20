def large_power(base, exponent):
    # Calculate base to the power of exponent
    result = base ** exponent
    
    # Check if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))

print(large_power(base, exponent))
