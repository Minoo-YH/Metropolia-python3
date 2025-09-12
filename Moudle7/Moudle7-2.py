names = set()


while True:
    raw = input("enter a name ( empty = stop):")
    name = raw.strip()
    if name =="" :
        break

    if name in names:
        print("Already exists")
    else:
        names.add(name)
        print("New name")

    print ()
    for n in names:
        print(n)