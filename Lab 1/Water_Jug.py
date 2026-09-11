jug1 = 4
jug2 = 3

a = 0
b = 0

while a != 2 and b != 2:

    if a == 0:
        a = jug1
        print(a, b)

    elif b == jug2:
        b = 0
        print(a, b)

    else:
        transfer = min(a, jug2 - b)
        a = a - transfer
        b = b + transfer
        print(a, b)

print("Target achieved!")