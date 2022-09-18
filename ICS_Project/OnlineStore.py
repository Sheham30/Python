list = [["shoes", 500],
        ["sandals", 400],
        ["t shirt", 100],
        ["hoodie", 800],
        ["trouser", 700],
        ["mobile", 5000],
        ["grocery", 1000],
        ["crockery", 1200],
        ["utensil", 600]
        ]
list2 = []


def rForReturn():
    r = 0
    while r != "r":
        r = input("\nPress r to return to home screen: ")
        if r == "r":
            break
        print("Invalid Choice")


def items():
    n = 1
    print("\tItems\t\t\tPrice")
    for i in list:
        print(f"{n}. {i[0]}\t\t\t{i[1]}")
        n += 1
    rForReturn()


def addItem():
    itemName = 0
    while itemName not in list:
        print("\n\t\t\t\t\t(Press r to return to home screen)")
        itemName = input("Enter item name: ").lower()
        for i in list:
            if itemName in i[0]:
                list.remove(i)
                list2.append(i)
                print("\nItem added to cart successfully")
                break
        if itemName not in i[0]:
            print("\nItem not available")
        if itemName == "r":
            break


def removeItem():
    itemName2 = 0
    while itemName2 not in list2:
        print("\n\t\t\t\t\t(Press r to return to home screen)")
        itemName2 = input("Enter item name: ").lower()
        for j in list2:
            if itemName2 in j[0]:
                list2.remove(j)
                list.append(j)
                print("Item removed from cart successfully")
                break
        if itemName2 not in j[0]:
            print("\nItem not available")
        if itemName2 == "r":
            break


def confirmOrder():
    while True:
        cO = input("Are you sure you want to confirm order (Yes or No ): ").lower()
        if cO == "no":
            print("\nOrder Not Confirmed")
            rForReturn()
            break
        elif cO == "yes":
            fileCreation()
            print("\nOrder confirmed...Exit program to view your file")
            list2.clear()
            rForReturn()
            break
        else:
            print("Invalid Choice")


def cart():
    total = 0
    if list2 == []:
        print("Cart is Empty")
    for i in list2:
        print(f"{i[0]}\t\t\t{i[1]}")
        total += i[1]
    print(f"\nTotal Price: {total}")
    rForReturn()


def fileCreation():
    f = input("\nEnter filename to save item: ")
    o = open(f"{f}.txt", "a")
    total = 0
    o.write("\n***Your Order***")
    for i in list2:
        o.write(f"\n {i[0]}\t\t\t{i[1]}")
        total += i[1]
    o.write(f"\n\nTotal Price: {total}")
    o.close()


welcome = '''
########Welcome to Online Store########

**************Home Screen**************

Choose the following option:
    1. Items
    2. Add Item to Cart
    3. Remove Item from Cart
    4. My Cart
    5. Confirm Order
    6. Exit'''

while True:
    print(welcome)
    s = input("\nEnter Option Number here: ")

    if s == "1":
        print("\n**************Items List***************")
        items()
    elif s == "2":
        print("\n***************Add Items***************")
        addItem()
    elif s == "3":
        print("\n*************Remove Items**************")
        removeItem()
    elif s == "4":
        print("\n****************My Cart****************")
        cart()
    elif s == "5":
        print("\n*************Confirm Order*************")
        confirmOrder()
    elif s == "6":
        exit()
        break
    else:
        print("\nInvalid Choice")
