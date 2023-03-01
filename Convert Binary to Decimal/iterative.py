def binToDecimal(binary):
    decimal = 0
    i = 0
    # Binary 10101101
    while binary > 0:
        last_digit = binary % 10 # Gives us the remainder
        decimal += last_digit * (2**i)
        binary = binary // 10   # Gives us the Quotient
        i += 1
    return decimal

binary = int(input("Enter a binary value: "))

print("Decimal equivalent: ", binToDecimal(binary))
