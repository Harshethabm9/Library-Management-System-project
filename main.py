class Student:
    def requestBook(self):
        print("So, you want to borrow book!")
        self.book = input("Enter name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        print("So, you want to return book!")
        name = input("Enter your name: ")
        self.book = input("Enter name of the book you want to return: ")
        if {name: self.book} in track:
            track.remove({name: self.book})
        return self.book

    def donateBook(self):
        print("\nOkay! You want to doante book!")
        self.book = input("\nEnter the name of the book you want to donate: ")
        return self.book

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        print(f"\n{len(self.books)} AVAILABLE BOOKS ARE: ")
        for book in self.books:
            print(" ♦-- " + book)
        print("\n")

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            print(
                f"{bookname} BOOK IS NOT AVAILABLE EITHER TAKEN BY SOMEONE ELSE, WAIT UNTIL HE RETURNED.\n")
        else:
            track.append({name: bookname})
            print("BOOK ISSUED!\nTHANK YOU KEEP IT WITH CARE AND RETURN ON TIME.\n")
            self.books.remove(bookname)

    def returnBook(self, bookname):
        print("BOOK RETURNED!\n THANK YOU! \n")
        self.books.append(bookname)

    def donateBook(self, bookname):
        print("BOOK DONATED! \nTHANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD.\n")
        self.books.append(bookname)

if __name__ == "__main__":

    myLibrary = Library(
        ["It all ends with us", "I am Krishna", "Rich and Poor Dad", "The Secrets of Nagas", "Macroeconomics", "Microeconomics", "Secrets"])
    student = Student()
    track = []

    print("\n WELCOME TO THE LIBRARY \n")
    # print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Show Listing of all books\n2. Borrow a book\n3. Return a book\n4. Donate a book\n5. Track Books\n6. Exit the library\n""")

    while (True):
        # print(track)
        try:
            print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Show Listing of all books\n2. Borrow a book\n3. Return a book\n4. Donate a book\n5. Track Books\n6. Exit the library\n""")
            usr_response = int(input("Enter your choice: "))

            if usr_response == 1:  # listing
                myLibrary.displayAvailableBooks()
            elif usr_response == 2:  # borrow
                myLibrary.borrowBook(
                    input("Enter your name: "), student.requestBook())
            elif usr_response == 3:  # return
                myLibrary.returnBook(student.returnBook())
            elif usr_response == 4:  # donate
                myLibrary.donateBook(student.donateBook())
            elif usr_response == 5:  # track
                for i in track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} book is taken/issued by {holder}.")
                print("\n")
                if len(track) == 0:
                    print("NO BOOKS ARE ISSUED!. \n")
            
            elif usr_response == 6: #exit
                print("THANK YOU ! \n")
                exit()
            else:
                print("INVAILD INPUT! \n")
        except Exception as e:              #catch errors
            print(f"Sorry! This is INVALID INPUT! \n")
