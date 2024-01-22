## UML 
Software engineers use UML, or Unified Modeling Language, a standardized modeling language, to visually depict a system's design. It offers a range of graphical notations and tools that facilitate communication, visualization, specification, construction, and documentation of software system artifacts between developers and stakeholders. 

### i. Class Diagram

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/9b08696c-f441-4631-901b-de6c513fe5a1)

* Student Class:

   - Attributes:
          book: str: Represents the current book the student is dealing with.
   - Methods:
          + requestBook(): str: Method for requesting a book. Returns the name of the book.
          + returnBook(): str: Method for returning a book. Returns the name of the book.
          + donateBook(): str: Method for donating a book. Returns the name of the book.
     
* Library Class:

    - Attributes:
          books: List[str]: Represents the list of books in the library.
    - Methods:
          + __init__(listofBooks: List[str]): Constructor method for initializing the library with a list of books.
          + displayAvailableBooks(): void: Method for displaying the available books in the library.
          + borrowBook(name: str, bookname: str): void: Method for borrowing a book. Updates the list of available books.
          + returnBook(bookname: str): void: Method for returning a book. Updates the list of available books.
          + donateBook(bookname: str): void: Method for donating a book. Updates the list of available books.
      
This diagram provides an overview of the classes, their attributes, and methods in the system.

### ii. Sequence Diagram for Borrowing a Book

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/8a8d68bb-531f-4878-a8ec-5e126eaf2245)

      Interaction Steps:
           - Student sends a requestBook() message to Library.
           - Library receives the message and calls the requestBook() method in Student.
           - Student provides the name of the book.
           - Library calls the borrowBook() method with the provided name.
           - Library updates the list of available books and adds the borrowing transaction to the Track.
           
This diagram illustrates the sequence of interactions between the Student and Library when a book is being borrowed.

### iii. Use Case Diagram

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/831024c8-46fa-4a30-80ca-2100c4843ba8)

    Library:
            Provides the following use cases:
              - Display Books
              - Borrow Book
              - Return Book
              - Donate Book
              
    Student:
            Provides the following use cases:
              - Borrow Book
              - Return Book
              - Donate Book
              
    Track:
            Provides the use case:
               - Track Issued Books
               
     Associations:
             - The Library uses the services provided by the Student and vice versa.
             - The Library interacts with the Track to track issued books.
             
This diagram shows the high-level interactions between users (students) and the system components (Library and Track) in terms of use cases.

### iv. Object Diagram

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/2e5c3cff-385e-4f57-8e7c-ef82323104d3)

      Library:
            Manages the library and books.
            
      Attributes:
            books: List of available books.
            
      Methods:
            __init__(listofBooks: List[str]): Constructor to initialize the library with a list of books.
            displayAvailableBooks(): void: Displays available books.
            borrowBook(name: str, bookname: str): void: Handles book borrowing.
            returnBook(bookname: str): void: Handles book return.
            donateBook(bookname: str): void: Handles book donation.

      Student:
            Represents a student interacting with the library.

      Attributes:
            book: Current book being tracked.
            
      Methods:
            requestBook(): str: Handles book request.
            returnBook(): str: Handles book return.
            donateBook(): str: Handles book donation.
            
      Associations:
      
      Library to Student:
            Uses a Student object for book-related interactions.
            Multiplicity: 1..*
      Student to Library:
            Has a reference to a Library object.
            Multiplicity: 1
            
This UML diagram provides a visual representation of the classes, their attributes, and their associations in the given code.

### v. Activity Diagram 

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/5f4001b8-2779-4a34-86e8-d78f7f8636d9)

- Choose Operation:
 User selects the operation: Borrow a book, Return a book, Donate a book.

- Borrow Book Activity:
 Sub-activity for borrowing a book.
 Includes entering user name, entering book name, checking availability, and issuing the book.

- Return Book Activity:
  Sub-activity for returning a book.
  Includes entering user name, entering book name, and receiving the returned book.

- Donate Book Activity:
   Sub-activity for donating a book.
   Includes entering user name, entering book name, and receiving the donated book.

This activity diagram illustrates the flow of activities in the Library Management System.

