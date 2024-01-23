# Library-management-system

This is a simple program on Libaray Management System where we have focused majorly on OOPs concept. It allows users to add books to the library, display available books, borrow a book from the available list of books, return a borrowed book bacK to library and track if a student donates a books to the library.

## Table of Contents

- [Features](##features)
- [Getting Started](##getting-started)
- [Git](##git)
- [Unified Modelling Language](###UML)
- [Requirement Engineering](##Requirement-Engineering)
- [Analysis Learning unit](##Analysis-Learning-unit)
- [Domain Driven Design](##ddd)
- [Metrics](##Metric)
- [Clean Code Development](##Clean-Code-Development)
- [Build Management](##Build-management)
- [Unit Tests](##Unit-tests)
- [Shortcuts of VSCode](##Shortcuts-of-VSCode)
- [License](##license)
  
  
## Features 

Book management: Add, update, and delete book entries, including details such as title and number of books available 

User Management: Register and maintain username and keep a track of books available in the library while keeping a record of return and issuance of books. 

Technologies Used
Programming Language: Python

## Getting Started

To get started with the Library Management System, follow these steps:

1. **Install Dependencies:**
   - Install Python and required libraries.

2. **Clone Repository:**
   - Clone the project repository from [repository link].

3. **Run the Application:**
   - Execute the main application file and you will see all the input and output in the console.
  


## 1. Git 

Library management system is upload on this repository :
[Library Management System](https://github.com/Harshethabm9/Library-Management-System-project)

The code of this project is upload on this repository:
[Project Source Code](https://github.com/Harshethabm9/Library-Management-System-project/blob/master/main.py)

## 2. UML

Here are few UML diagrams including Class Diagram , Sequence Diagram and Use Case Diagram for this project  
[Unified Modeling Language](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/uml.md)


## 3. Requirement Engineering 
[Jira](https://library-book.atlassian.net/jira/software/projects/LMS/boards/1)

![WhatsApp Image 2024-01-23 at 14 43 05_15d14535](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/21ccbfc5-47c7-49d3-a9f2-6db78f1fd4d8)


[Trello](https://trello.com/b/XzbUHKyZ/my-trello-board)

![WhatsApp Image 2024-01-23 at 14 43 05_0415e5ff](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/93cf9c62-d4b9-4d6b-836e-2c6a1ced3beb)


[Notion](https://www.notion.so/ff0f85f758a34978b815ddfa1d252b8e?v=ddf1d5bb82d84fb29a32cd9a3ca13e8b)

![WhatsApp Image 2024-01-23 at 14 43 04_f17d1cd5](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/8ae722a4-7c1c-4dfb-94d4-a726896b000b)


Requirements Engineering by mapping for this code 

[Requirement Engineerring](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/req_engineering.md)

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


## 5. DDD (Domain Driven Design)

In domain-driven design (DDD), domains within a system are identified and arranged, the core domain is highlighted, and a strategy design outlining the interactions and mappings between these domains is created. We may find possible domains in the code that is supplied, develop a strategic design, and then document it. 

[Doamin Driven Design](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/DDD.md)

[Core Domain Chart](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/Blank%20board%20-%20Page%201%20Frame%201%20(1).jpeg)


## 6. Metrics 

[Metrics](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/metrics.md)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=Harshethabm9_Library-management-system&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=Harshethabm9_Library-management-system)


## 7. Clean Code Development

The clean code pratices followed in this code are :

i. Meaningful Variable and Method Names: 
Choose meaningful and self-explanatory names that convey the purpose of the variable or method.
Example: user_choice = int(input("Enter your choice: "))

ii.  Consistent Code Formatting: 
I have maintained consistent indentation and spacing throughout the code.

iii. Use of Constants: 
I have used constants to improve code readability.

iv. Encapsulation:
I have created separate class for all functions.

v. User Interaction
Improve user interaction by providing clear prompts and messages.

## Build Management 

[Build Management](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/Build_management.md)

## 9. Unit Test

[Few Unit Test](https://github.com/Harshethabm9/Library-Management-System-project/blob/main/unit_tests.md)


## 10. Shortcuts of VSCode

Alt + Click: Insert cursor(Multiple cursor)
Shift + Alt + F: Format document
Ctrl + Enter: Insert line below
Ctrl + N: New File
Ctrl + X: Cut line
Ctrl + C: Copy line 
Ctrl + S : Save all

## License
 
This project Library management system is privately owned by Harshetha Murthy , a student at SRH Berlin University of Applied Sciences pursuing an MSc in Computer Science with a specialization in Big Data and Artificial Intelligence.
 
**Contact Information:**
- **Name**: Harshetha Murthy
- **Email**: harshethabm@gmail.com
