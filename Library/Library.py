
myList = []
list = ["aa", "bb", "cc", "dd"]

def bookList(a):
    if a == "1":
        for i in list:
            print(i)
    else:
        pass

def borrowBook(a):
    if a == "2":
        bookName = input("Enter name of book: ")
        if bookName in list:
            list.remove(bookName)
            print("Book borrowed successfully")
            myList.append(bookName)
        else:
            print("Book is not available")

def returnBook(a):
    if a == "3":
        bookName2 = input("Enter name of book: ")
        if bookName2 in list:
            print("Book is already here")
        elif bookName2 not in list:
            list.append(bookName2)
            print("Book added successfully")
        elif bookName2 in myList:
            myList.remove(bookName2)
        else:
            pass

def myBooks(a):
    if a == "5":
        for j in myList:
            print(j)
    else:
        pass


welcome = '''
*****Welcome to LIbrary****

Choose any Option
1. Books List
2. Take Book
3. Return Book
4. Exit
5. My books
            press b for back'''





print(welcome)
while True:
    b = input("\nEnter: ")
    if b == "b":
        print(welcome)

    if b == "4":
        exit()
    # else:
    #     print("Invalid Choice")

    bookList(b)
    borrowBook(b)
    returnBook(b)
    myBooks(b)

