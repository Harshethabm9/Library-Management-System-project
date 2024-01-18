# Library-management-system
This is a simple program on Libaray Management System where we have focused majorly on OOPs concept. It allows users to add books to the library, display available books, borrow a book from the available list of books, return a borrowed book bacK to library and track if a student donates a books to the library.
 
## Overview
A library management system is a software application for efficiently managing library operations and resources. It serves as a comprehensive tool for librarians, allowing them to streamline book management, user interaction, and administrative tasks. 

## Features 

Book management: Add, update, and delete book entries, including details such as title and number of books available 

User Management: Register and maintain username and keep a track of books available in the library while keeping a record of return and issuance of books. 

Technologies Used
Programming Language: Python

## 1. Git 

Library management system is upload on this respository :
https://github.com/Harshethabm9/Library-Management-System-project 

## 2. UML

Software engineers use UML, or Unified Modeling Language, a standardized modeling language, to visually depict a system's design. It offers a range of graphical notations and tools that facilitate communication, visualization, specification, construction, and documentation of software system artifacts between developers and stakeholders. Here are three UML diagrams:

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

### iii. Use Caase Diagram

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

## 3. Required Engineering 

**Project: Library Management System**

i. Requirements Identification:
Let's identify a few high-level requirements for our Library Management System:

User Interaction:
          Users should be able to browse available books, borrow books, return books, and donate books.
          
Tracking:
          The system should track books that are borrowed by users.
          

ii. Jira - Requirements Mapping:

In Jira, we can create user stories and epics:

#### Epic: User Interaction

          User Story 1: As a user, I want to see a list of available books, so I can browse and choose a book to borrow.
          User Story 2: As a user, I want to borrow a book, so I can read it.
          User Story 3: As a user, I want to return a book, so others can borrow it.
          User Story 4: As a user, I want to donate a book to the library.
#### Epic: Tracking
          User Story 5: As a librarian, I want to track books borrowed by users, so I can manage the library inventory.


iii. Trello - Requirements Mapping:
   
In Trello, we can create boards and cards:
        Board: Library Management System Features

#### List: User Interaction

        Card 1: Browse Available Books 
        Card 2: Borrow a Book
        Card 3: Return a Book
        Card 4: Donate a Book
#### List: Tracking
        Card 5: Track Borrowed Books

## 4. Analysis Learning unit

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
   - Install Python and required libraries.

2. **Clone Repository:**
   - Clone the project repository from [repository link].

3. **Run the Application:**
   - Execute the main application file and you will see all the input and output in the console.
  


### Few Gilmpse of the project 

1. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/2a588e29-322b-4d2c-9653-63bc3985b5ad)
2. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/ff80216a-9a36-4a6c-9b66-9238ab1d6a68)
3. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/dece6ff0-faac-47c2-962e-47b0c5e7db15)
4. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/7a4d3afe-90ba-4a98-801c-d33a39b15399)
5. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/8aca983d-8d0b-4da7-b57a-54a73cdc0608)
6. ![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/56167857-bec2-416b-ba46-32263ddfae63)

## 5. DDD (Domain Driven Design)

In domain-driven design (DDD), domains within a system are identified and arranged, the core domain is highlighted, and a strategy design outlining the interactions and mappings between these domains is created. We may find possible domains in the code that is supplied, develop a strategic design, and then document it.

### Identify Domains:

  Library Domain:
                 - Responsible for managing the library, available books, and book transactions.
                 - Includes the Library class.
  
  Student Domain:
                 - Represents the actions and information related to students borrowing, returning, and donating books.
                 - Includes the Student class.
                 
   Tracking Domain:
                 - Manages the tracking of book transactions, such as books borrowed by students.
                 -Includes the Track class.

    Strategic Design:
![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/01883235-43d1-4094-b39f-cd9056d02962)

     Core Domain (Library):
                 - Manages the core functionality of the library, including book management and transactions.
                 - The Library class encapsulates the core domain.
                 
     Supporting Domains (Student and Track):
                 - The Student class supports the core domain by handling user interactions related to books (requesting, returning, donating).
                 - The Track class supports the core domain by tracking book transactions (issued books).

## 6. Metrics 

### Metric 1: Cyclomatic Complexity

**Objective: Measure the complexity of the code by assessing the number of independent paths through the program.**

    Calculation:
         - Use a code analysis tool, such as radon or McCabe complexity checker, to calculate the cyclomatic complexity.
         - The metric is typically represented as a single numeric value.

    Interpretation:
         - A lower cyclomatic complexity indicates simpler and more maintainable code.
         - Higher values suggest more complex code that may be harder to understand and maintain.
         
### Metric 2: Maintainability Index
**Objective: Provide an overall indication of how maintainable the code is based on various factors.**

        Calculation:
            - Use a code analysis tool, such as radon or other static code analyzers, to calculate the maintainability index.
            - The maintainability index is often presented as a score on a scale (e.g., 0 to 100).
            
         Interpretation:
             - Higher maintainability index values indicate more maintainable code.
             - Lower values suggest code that may be challenging to maintain.
             
#### Implementation:
For the code provided, you can use tools like radon to calculate these metrics.

    1. Cyclomatic Complexity:
        Tools:
            radon (installable via pip: pip install radon).
            Calculation Example:
            Run radon cc -s library_management_system.py to get cyclomatic complexity values.
     2. Maintainability Index:
         Tools:
             radon (installable via pip: pip install radon).
             
Benefits:
These metrics help gauge the complexity and maintainability of the code.
They provide insights into potential areas for refactoring or improvement.



                   


## License
 
This project Library management system is privately owned by Harshetha Murthy , a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.
 
**Contact Information:**
- **Name**: Harshetha Murthy
- **Email**: harshethabm@gmail.com
