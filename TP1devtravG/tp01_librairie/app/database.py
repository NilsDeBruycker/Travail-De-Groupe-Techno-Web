from datetime import date
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
    ]
}
