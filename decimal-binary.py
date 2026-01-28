num = int(input("Enter a decimal number: "))
n = num
convert = ""

while n > 0:
    remainder = n % 2
    n = n // 2
    for _ in range(1):
        convert = str(remainder) + convert

print("Binary of", num, "is:", convert)
