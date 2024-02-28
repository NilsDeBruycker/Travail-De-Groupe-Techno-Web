from app.schemas import Book
from app.database import database


def save_book(new_book: Book) -> Book:
    database["books"].append(new_book)
    return new_book


def get_all_books() -> list[Book]:
    books_data = database["books"]
    books = [Book.model_validate(data) for data in books_data]
    return books


def get_book_by_id(book_id: str) -> Book | None:
    selected_book = [
        book for book in database["books"]
        if book["id"] == book_id
    ]
    if len(selected_book) < 1:
        return None
    selected_book = Book.model_validate(selected_book[0])
    return selected_book
    
def delete_book_by_id(book_id:str):
    for book in database["books"]:
        if book["id"] == book_id:
            del database[book_id]



def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    modified_books = []

    # Iterate through the existing books in the database
    for book in database["books"]:
        # Check if the book has the specified ID
        if book["id"] == book_id:
            # Check if the ID of the modified book is different from the original book
             # You might want to handle this case accordingly

            # Update the book data with the new modified book data
            # Modify the book content
            """modified_book = Book(
                id=book_id,
                name=[,
                Author=book["author"],
                Editor=book["edittor"]"""
            
            # Append the modified book to the list
            modified_books.append(modified_book)

    # Replace the old database with the new list of modified books
    i=0
    for book in database["books"]:
        if book["id"]==book_id:
            database["books"][i] =modified_book 
        i+=1

