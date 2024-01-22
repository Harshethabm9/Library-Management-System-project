## Few unit tests 

### i.Test for display available Books

   def test_display_available_books(self):
      with self.assertLogs(level='INFO') as cm:
         self.library.displayAvailableBooks()
      self.assertIn('INFO:root:3 AVAILABLE BOOKS ARE:', cm.output)

### ii. Test for books not available 

    def test_borrow_book_unavailable(self):
        book_to_borrow = "unavailable_book"
        student_name = "John Doe"
        with unittest.mock.patch("builtins.input", side_effect=[student_name]):
            with self.assertLogs(level='INFO') as cm:
                self.library.borrowBook(student_name, book_to_borrow)
            self.assertIn(f'INFO:root:{book_to_borrow} BOOK IS NOT AVAILABLE', cm.output)

### iii. Test for Borrow book

      def test_borrow_book_success(self):
        book_to_borrow = "book1"
        student_name = "John Doe"
        with unittest.mock.patch("builtins.input", side_effect=[student_name]):
            self.library.borrowBook(student_name, book_to_borrow)
            self.assertNotIn(book_to_borrow, self.library.books)
            self.assertIn({student_name: book_to_borrow}, track)

