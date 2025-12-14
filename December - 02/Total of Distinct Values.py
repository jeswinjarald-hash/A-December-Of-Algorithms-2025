N = int(input("Enter a number: "))

width = len(bin(N)[2:])

print(f"{'DECIMAL':<{width}} {'OCTAL':<{width}} {'HEX':<{width}} {'BINARY':<{width}}")

for i in range(1, N+1):
    dec = str(i)
    octal = oct(i)[2:]
    hexa = hex(i)[2:].upper()
    binary = bin(i)[2:]

    print(f"{dec:<{width}} {octal:<{width}} {hexa:<{width}} {binary:<{width}}")
