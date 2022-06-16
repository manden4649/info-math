

char = []
i = 0
""" while True:
    char.append(int(input(f"[{i}] = ")))
    if char[i] == 0:

    i += 1 """


n = int(input("pls input n = "))
e = int(input("pls input e = "))
P = int(input("pls input P = "))

a = int(P ** e)
a = a % n

print(f"C = {a}")