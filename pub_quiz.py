a, b = 250, 250

for _ in range(250, 260):
    if a is not b:
        break

    a += 1
    b += 1

    print("==========")
    print(_)
    print("ID A:")
    print(id(a))
    print("ID B:")
    print(id(b))

print(">>> outside of the for <<<")
print(a)
