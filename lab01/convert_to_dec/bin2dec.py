def bin_to_dec(digit):
    length = len(digit)
    number = 0
    for i in range(0, length):
        number = number + int(digit[i])*(2**(length-i-1)) #an*2n-1+an-1*2n-2+...+a0*20
    return number

a = input("Двоичное число:")
print(f"Двоичное число {a}, равно десятичному числу {bin_to_dec(a)}")