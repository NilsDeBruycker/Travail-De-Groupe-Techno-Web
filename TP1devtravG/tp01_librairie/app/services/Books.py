from app.schemas import Book
from app.database import database


def save_book(new_book: Book) -> Book:
    database["books"].append(new_book)
    return new_book


def get_all_books() -> list[Book]:
    books_data = database["books"]
    books = [Book.model_validate(data) for data in books_data]
    
    return books


    
def delete_book_by_id(book_id:str):
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
            del database["books"][i]
        i+=1
def is_book_exist(book_id:str):
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:

            return True
        i+=1
    return False

def modify_book_by_id(book_id: str,modified_book) -> Book | None:
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
            database["books"][i] =modified_book 
        i+=1
def is_book_exist(book_id:str):
    i=0
    for book in database["books"]:
        if  database["books"][i]["id"]== book_id:
    
            return True
        else: i+=1
    return False