from uuid import uuid4


database = {
    "books": [
        {
            "id": str(uuid4()),
            "name": "Frankestein",
            "Author": "mary shelley",
            "Editor": "Marvor & Jones",
        },
        {
            "id": str(uuid4()),
            "name": "tintin",
            "Author": "hergé",
            "Editor": "dupuis",
        },
        {
            "id": str(uuid4()),
            "name": "toto",
            "Author": "jean renaud",
            "Editor": "edition libre",
        },
       { 
        "id": str(uuid4()),
        "name": "Le Seigneur des Anneaux",
        "Author": "J.R.R. Tolkien",
        "Editor": "Christian Bourgois Éditeur"
        },
        {
        "id": str(uuid4()),
        "name": "Harry Potter à l'école des sorciers",
        "Author": "J.K. Rowling",
        "Editor": "Gallimard Jeunesse"
        },
        {
        "id": str(uuid4()),
        "name": "1984",
        "Author": "George Orwell",
        "Editor": "Gallimard"
        },
        {
        "id": str(uuid4()),
        "name": "Le Petit Prince",
        "Author": "Antoine de Saint-Exupéry",
        "Editor": "Gallimard"
        },
        {
        "id": str(uuid4()),
        "name": "L'Alchimiste",
        "Author": "Paulo Coelho",
        "Editor": "Anne Carrière"
        }
    ],
    "users":[
            {"username":"jon",
            "email":"arbucle@gmail.com",
            "password":"1234",
            "role":"normal",
            "blocked": False},
            {"username":"joseph",
            "email":"joseph@gmail.com",
            "password":"5482",
            "role":"admin",
            "blocked" :False},
            {
               "username": "that_guy",
               "email":"realAmaz0n",
               "password":"4795",
                "blocked":True}
    ]
}
