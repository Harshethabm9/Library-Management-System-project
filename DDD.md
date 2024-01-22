## Domain Driven Design 

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

### Strategic Design:
![image](https://github.com/Harshethabm9/Library-Management-System-project/assets/148848257/01883235-43d1-4094-b39f-cd9056d02962)

     Core Domain (Library):
                 - Manages the core functionality of the library, including book management and transactions.
                 - The Library class encapsulates the core domain.
                 
     Supporting Domains (Student and Track):
                 - The Student class supports the core domain by handling user interactions related to books (requesting, returning, donating).
                 - The Track class supports the core domain by tracking book transactions (issued books).

