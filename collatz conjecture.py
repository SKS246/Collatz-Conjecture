x = int(input("Number: "))
iterations = 0

while x != 1:
    if x % 2 == 1:
        x = (3 * x) + 1
        print(x)
    elif x % 2 == 0:
        x = x/2
        print(x)
    iterations += 1

print("Iterations: " + str(iterations))
