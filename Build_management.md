## 8. Build Management 

To introduce build management, documentation generation, testing, and CI/CD to the "Library Management System", we will use 'setuptools' for build management, 'Sphinx' for documentation generation, and 'pytest' for testing.

### i.Build Management with 'setuptools'

- Install 'setuptools'
  
     pip install setuptools
  
- Create a file for 'setup.py'
  
  from setuptools import setup
  setup(
    name='LibraryManagementSystem',
    version='0.1',
    packages=[''],
   )
  
- Build the project
  
   python setup.py sdist
  
This will create a dist directory with a source distribution of your project.
 
### ii.Documentation Generation with Sphinx

- Install 'Sphinx'
     pip install sphinx

- Generate Documentation
     sphinx-quickstart
  
- After configuration, run:
     make html
  
Open the generated HTML documentation in _build/html/index.html.

### iii. Testing with pytest

- Install 'pytest'
     pip install pytest

- Write test cases
  
     from library import Library
     def test_display_available_books(capsys):
       library = Library(["book1", "book2"])
       library.displayAvailableBooks()
       captured = capsys.readouterr()
       assert "2 AVAILABLE BOOKS ARE:" in captured.out

- Run pytest

