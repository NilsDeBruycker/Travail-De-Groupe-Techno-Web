from datetime import date
from uuid import uuid4


database = {
    "books": [
        {
            "id": str(uuid4()),
            "name": "Faire mon exercice de techno-web !",
            "Author": "Ilil",
            "Editor": "date(year=2024, month=1, day=21)",
        },
        {
            "id": str(uuid4()),
            "name": "Sortir le chien",
            "Author": "N'oub",
            "Editor": "date(year=2024, month=1, day=15)",
        },
        {
            "id": str(uuid4()),
            "name": "Rendre les cartes pokemons à Titouan",
            "Author": "Il a peu",
            "Editor": "date(year=2023, month=12, day=27)",
        },
    ]
}
