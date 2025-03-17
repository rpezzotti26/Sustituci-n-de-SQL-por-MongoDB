import database
from bson.objectid import ObjectId

def add_book():
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado_lectura = input("Estado (leído/no leído): ")
    database.add_book(titulo, autor, genero, estado_lectura)

def update_book():
    book_id = input("ID del libro a actualizar: ")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado_lectura = input("Estado (leído/no leído): ")
    database.update_book(book_id, titulo, autor, genero, estado_lectura)

def delete_book():
    book_id = input("ID del libro a eliminar: ")
    database.delete_book(book_id)

def list_books():
    books = database.list_books()
    for book in books:
        print(f"ID: {book['_id']}, Título: {book['titulo']}, Autor: {book['autor']}, Género: {book['genero']}, Estado: {book['estado_lectura']}")

def search_books():
    query = input("Buscar: ")
    field = input("Buscar por (titulo/autor/genero): ")
    books = database.search_books(query, field)
    for book in books:
        print(f"ID: {book['_id']}, Título: {book['titulo']}, Autor: {book['autor']}, Género: {book['genero']}, Estado: {book['estado_lectura']}")