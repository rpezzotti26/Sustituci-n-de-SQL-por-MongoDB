from bson import ObjectId
from pymongo import MongoClient

CONNECTION_STRING = "tu_cadena_de_conexion_de_mongodb_atlas"
client = MongoClient(CONNECTION_STRING)
db = client["biblioteca_personal"]  # Nombre de la base de datos
collection = db["libros"]  # Nombre de la colección

def add_book(titulo, autor, genero, estado_lectura):
    book = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado_lectura": estado_lectura,
    }
    collection.insert_one(book)

def update_book(book_id, titulo, autor, genero, estado_lectura):
    collection.update_one(
        {"_id": ObjectId(book_id)},
        {
            "$set": {
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "estado_lectura": estado_lectura,
            }
        },
    )

def delete_book(book_id):
    collection.delete_one({"_id": ObjectId(book_id)})

def list_books():
    return list(collection.find())

def search_books(query, field):
    return list(collection.find({field: {"$regex": query, "$options": "i"}}))