from uuid import uuid4 # Import file UUID lib bawaan py
from app.database import Database

class Todo:
    # Pada method constructor, kita punya dua atribut yaitu db_name dan database. Atribut db_name ini kita simpan untuk nama database todo yang kita punya, sedangkan atribut database kita pakai sebagai tempat inisiasi class Database yang tadi kita buat. Karena parameter pada class database adalah db, kita bisa dengan mudah memasukkan nilai ke parameter tersebut dengan memanggil nama parameternya seperti contoh di atas.
    def __init__(self):
        self.db_name = "todo-db.txt"
        self.database = Database(db=self.db_name)  # Inisialisasi class Database dengan nama db yang kita siapkan

    def create(self, title: str, desc: str):
        todo = {
            "id": str(uuid4()), # Buat ID unique
            "title": title,
            "desc": desc
        }

        self.database.insert(todo) # Manggil fungsi insert untuk dimasukkan ke db

    def read(self):
        todos = self.database.read() # Manggil fungsi baca db

        for todo in todos: # Mencetak data dengan looping karena yang dikembalikan adalah tipe data array (list)
            print(f"\n---------------------------------")
            print(f"ID: {todo['id']}")
            print(f"Title: {todo['title']}")
            print(f"Description: {todo['desc']}")
            print(f"--------------------------------")

    def get_by_id(self, id: str):
        todo = self.database.get_by_id(id)

        if not todo.get('data'):
            print("\nTodo tidak ditemukan!\n")
            return
        
        return todo.get('data')