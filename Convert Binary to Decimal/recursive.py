def binToDecimal(binary):
    if binary == 0:
        return 0
    # Binary = 1011
    else:
        return (binary % 10 + 2*(binToDecimal(binary // 10)))
    
binary = int(input("Enter a binary value: "))

print("Decimal Equivalent: ", binToDecimal(binary))