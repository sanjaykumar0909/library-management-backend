from datetime import datetime
from mainapp.models import Library  # Import the Library model

def run():
    def push_to_database(data):
        # Extract values from the data dictionary
        book_id = data['bookId']
        book_name = data['bookName']
        author = data['author']
        publish_date = datetime.strptime(data['publishDate'], '%Y-%m-%d')  # Convert string to datetime
        available = data['available']

        # Create an instance of the Library model with the extracted values
        library_instance = Library(
            bookId=book_id,
            bookName=book_name,
            author=author,
            publishDate=publish_date,
            available=available
        )

        # Save the instance to the database
        library_instance.save()

    data = [
        {"bookId": 1, "bookName": 'Harry Potter', "author": "J.K. Rowling", "available": 21,
         "publishDate": "2000-06-26"},
        {"bookId": 2, "bookName": 'Percy Jackson & the Olympians: The Lightning Thief', "author": "Rick Riordan",
         "available": 14, "publishDate": "2005-06-28"},
        {"bookId": 3, "bookName": 'The Hobbit', "author": 'J.R.R. Tolkien', "available": 30,
         "publishDate": "1937-09-21"},
        {"bookId": 4, "bookName": 'To Kill a Mockingbird', "author": 'Harper Lee', "available": 10,
         "publishDate": "1960-07-11"},
        {"bookId": 5, "bookName": '1984', "author": 'George Orwell', "available": 7, "publishDate": "1949-06-08"},
        {"bookId": 6, "bookName": 'The Catcher in the Rye', "author": 'J.D. Salinger', "available": 28,
         "publishDate": "1951-07-16"},
        {"bookId": 7, "bookName": 'The Great Gatsby', "author": 'F. Scott Fitzgerald', "available": 15,
         "publishDate": "1925-04-10"},
        {"bookId": 8, "bookName": 'The Lord of the Rings: The Fellowship of the Ring', "author": 'J.R.R. Tolkien',
         "available": 20, "publishDate": "1954-07-29"},
        {"bookId": 9, "bookName": 'The Hunger Games', "author": 'Suzanne Collins', "available": 25,
         "publishDate": "2008-09-14"},
        {"bookId": 10, "bookName": 'The Chronicles of Narnia: The Lion, the Witch and the Wardrobe',
         "author": 'C.S. Lewis', "available": 12, "publishDate": "1950-10-16"},
        {"bookId": 11, "bookName": 'The Da Vinci Code', "author": 'Dan Brown', "available": 18,
         "publishDate": "2003-03-18"},
        {"bookId": 12, "bookName": 'The Alchemist', "author": 'Paulo Coelho', "available": 22,
         "publishDate": "1988-09-01"},
        {"bookId": 13, "bookName": 'The Girl with the Dragon Tattoo', "author": 'Stieg Larsson', "available": 17,
         "publishDate": "2005-08-01"},
        {"bookId": 14, "bookName": 'The Fault in Our Stars', "author": 'John Green', "available": 9,
         "publishDate": "2012-01-10"},
        {"bookId": 15, "bookName": 'The Kite Runner', "author": 'Khaled Hosseini', "available": 16,
         "publishDate": "2003-05-29"},
        {"bookId": 16, "bookName": 'The Shining', "author": 'Stephen King', "available": 11,
         "publishDate": "1977-01-28"},
        {"bookId": 17, "bookName": 'Gone with the Wind', "author": 'Margaret Mitchell', "available": 27,
         "publishDate": "1936-06-30"},
        {"bookId": 18, "bookName": 'The Book Thief', "author": 'Markus Zusak', "available": 8,
         "publishDate": "2005-03-14"},
        {"bookId": 19, "bookName": 'Brave New World', "author": 'Aldous Huxley', "available": 19,
         "publishDate": "1932-06-01"},
        {"bookId": 20, "bookName": 'The Picture of Dorian Gray', "author": 'Oscar Wilde', "available": 23,
         "publishDate": "1890-07-20"},
        {"bookId": 21, "bookName": 'The Road', "author": 'Cormac McCarthy', "available": 13,
         "publishDate": "2006-09-26"},
        {"bookId": 22, "bookName": 'Moby-Dick', "author": 'Herman Melville', "available": 26,
         "publishDate": "1851-10-18"},
        {"bookId": 23, "bookName": 'The Adventures of Sherlock Holmes', "author": 'Arthur Conan Doyle', "available": 6,
         "publishDate": "1892-10-14"},
        {"bookId": 24, "bookName": 'Frankenstein', "author": 'Mary Shelley', "available": 24,
         "publishDate": "1818-01-01"},
        {"bookId": 25, "bookName": 'The Stand', "author": 'Stephen King', "available": 29, "publishDate": "1978-09-01"},
    ]
    for i in data:
        push_to_database(i)