#Write a menu driven program that keeps record of books and journals available in a library.
# Define two methods read() and display()
#In read() method user has to read title, author and price of a book. In display() method display book details
# such as title, author and price.

class library:
    '''def __init__(self):
        self.title = ""
        self.author = ""
        self.publisher = ""'''

    def read(self):
        self.title = input("Enter Book Title: ")
        self.author = input("Enter Book author: ")
        self.publisher = input("Enter Book Publisher: ")

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Publisher:", self.publisher)
        print("\n")


my_book = []
ch = 'y'
while (ch == 'y'):
    print('''
1. Add New Book
2. Display Books
''')
    choice = int(input("Enter choice: "))
    if (choice == 1):
        book = library()
        book.read()
        my_book.append(book)
        #print(my_book[0])
    elif (choice == 2):
        for i in my_book:
            i.display()
    else:
        print("Invalid choice!")
    ch = input("Do you want to continue..?")
print("Bye!")



