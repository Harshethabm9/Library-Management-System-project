# Library-management-system
This is a simple program on Libaray Management System where we have focused majorly on OOPs concept. It allows users to add books to the library, display available books, borrow a book from the available list of books, return a borrowed book bacK to library and track if a student donates a books to the library.
 
## Overview
A library management system is a software application for efficiently managing library operations and resources. It serves as a comprehensive tool for librarians, allowing them to streamline book management, user interaction, and administrative tasks. 

Features 

Book management: Add, update, and delete book entries, including details such as title and number of books available 

User Management: Register and maintain username and keep a track of books available in the library while keeping a record of return and issuance of books. 

Technologies Used
Programming Language: Python

## Features

1. **Book Management:**
   - Add, update, and remove book from list of the books.
   - Record details such as Books name and username who have borrowed it.

2. **User Management:**
   - Handle borrowing, donation and returns.

3. **Cataloging & Search:**
   - user can see all the listing of the books available in Console.

4. **Borrowing & Returns:**
   - Facilitate the process of lending and returning books.


5. **Reporting & Analytics:**
   - Show all the books issued, borrowed and track all the books availabel in the library.

## Getting Started

To get started with the Library Management System, follow these steps:

1. **Install Dependencies:**
   - Install Python/C++ and required libraries.

2. **Clone Repository:**
   - Clone the project repository from [repository link].

3. **Run the Application:**
   - Execute the main application file and you will see all the input and output in the console.

## Few Gilmpse of the project 

1. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/2a588e29-322b-4d2c-9653-63bc3985b5ad)
2. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/ff80216a-9a36-4a6c-9b66-9238ab1d6a68)
3. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/dece6ff0-faac-47c2-962e-47b0c5e7db15)
4. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/7a4d3afe-90ba-4a98-801c-d33a39b15399)
5. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/8aca983d-8d0b-4da7-b57a-54a73cdc0608)
6. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/56167857-bec2-416b-ba46-32263ddfae63)

## UML

Software engineers use UML, or Unified Modeling Language, a standardized modeling language, to visually depict a system's design. It offers a range of graphical notations and tools that facilitate communication, visualization, specification, construction, and documentation of software system artifacts between developers and stakeholders. Here are three UML diagrams:

### 1. Class Diagram

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

### 2. Sequence Diagram for Borrowing a Book

![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/8a8d68bb-531f-4878-a8ec-5e126eaf2245)

      Interaction Steps:
           - Student sends a requestBook() message to Library.
           - Library receives the message and calls the requestBook() method in Student.
           - Student provides the name of the book.
           - Library calls the borrowBook() method with the provided name.
           - Library updates the list of available books and adds the borrowing transaction to the Track.
           
This diagram illustrates the sequence of interactions between the Student and Library when a book is being borrowed.

### 3. Use Caase Diagram

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

## License
 
This project Library management system is privately owned by Harshetha Murthy , a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.
 
**Contact Information:**
- **Name**: Harshetha Murthy
- **Email**: harshethabm@gmail.com
