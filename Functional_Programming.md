## Funtional Programming
In functional programming, data is immutable, and functions are first-class citizens, allowing for concise, declarative code that is often easier to reason about and parallelize. It emphasizes immutability, pure functions without side effects, and higher-order functions. All though this project source do not 

### 1. Only Final Data Structures:
In functional programming, data structures are often immutable. The Library class in the code is implemented with an immutable data structure. The borrow_book, return_book, and donate_book methods create and return new instances of the Library class instead of modifying the existing instance. This ensures immutability.

      class Library:
          def __init__(self, books: List[str]):
              self.books = books
      
          def borrow_book(self, name: str, bookname: str) -> Union[str, 'Library']:
              # ...
              updated_books = [b for b in self.books if b != bookname]
              return f"BOOK ISSUED! THANK YOU, {name}.", Library(updated_books)
      
          def return_book(self, bookname: str) -> 'Library':
              return Library(self.books + [bookname])
      
          def donate_book(self, bookname: str) -> 'Library':
              return Library(self.books + [bookname])


### 2.  (Mostly) Side-Effect-Free Functions:
While not all functions in the code are side-effect-free due to user input/output operations, efforts have been made to minimize side effects. The methods like borrow_book, return_book, and donate_book are side-effect-free in terms of the Library object; they create and return new instances without modifying the existing state directly.

        def student_request_book() -> str:
            # ...
        
        def student_return_book() -> Tuple[str, str]:
            # ...
        
        def student_donate_book() -> str:
            # ...

### 3. Use of Higher-Order Functions:
A higher-order function is a function that takes other functions as parameters or returns functions as results. In the code, the display_available_books method can be considered a higher-order function. It takes no arguments but performs an action, which is to print the available books.

        class Library:
            def display_available_books(self):
                # ...

### 4. Functions as Parameters and Return Values:
Functions are used as parameters and return values in the following examples:

The main function interacts with user-defined functions such as student_request_book, student_return_book, and student_donate_book.
            def main():
                # ...
                book = student_request_book()
                # ...
                name, book = student_return_book()
                # ...
                book = student_donate_book()
                # ...

### 5. Use of Closures / Anonymous Functions:
The code does not explicitly use closures or anonymous functions. However, in languages like Python, lambda functions can be used as anonymous functions. We can add a lambda function to our borrow_book function as:
             def borrow_book(self, name: str, bookname: str) -> Union[str, 'Library']:
                    if bookname not in self.books:
                        return f"{bookname} BOOK IS NOT AVAILABLE OR TAKEN BY SOMEONE ELSE."
                    else:
                        updated_books = list(filter(lambda b: b != bookname, self.books))
                        return f"BOOK ISSUED! THANK YOU, {name}.", Library(updated_books)

In this modification, the lambda function is used within the borrow_book method to filter out the book being borrowed. The filter function takes the lambda function as a condition, creating a more concise expression.

### 6. Coverage Outside the Code:
The provided code is written in Python. While Python supports functional programming concepts, but languages like F#, Clojure, Julia, etc., are designed with functional programming principles in mind. In those languages, you might find more advanced features and idioms specific to functional programming. So to implement full Functional Programming Concept, we will create a code in F# through which we can attain a functional programming.

[Funtional Programming f# Source Code](https://github.com/Harshethabm9/Library-Management-System-project/blob/master/Functional_programming.fs)

In this F# version:
- The Library type is immutable.
- Functions like borrowBook, returnBook, and donateBook return new instances of Library.
- List.filter is used for immutably updating the list of books.
- Higher-order functions are used for iteration and filtering.
- Pattern matching is used for control flow.
- 
This F# code embraces functional programming principles, making the code concise and leveraging the strengths of the F# language.








