
def divisible_by_ten(num):
    # Check if the remainder of num divided by 10 is 0
    if num % 10 == 0:
        return True
    else:
        return False


print(divisible_by_ten(50))  # Should return True because 50 is divisible by 10
print(divisible_by_ten(23))  # Should return False because 23 is not divisible by 10
