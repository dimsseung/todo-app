import json

class Database:
    # fungsi init nerima param db tipe string yg gunanya utk nerima param string 
    # yg bisa kita gunin untuk penyimpnan db txt
    def __init__(self, db: str = 'database-todo.txt'):
        self.db: str = db

    # fungsi insert pake fungsi bawaan py. param 'a' tujuannya buat data baru trus ditambahin ke baris plg akhir
    # klau pke 'w' nnti malah nulis ulang dari awal
    def insert(self, data: dict):
        with open(self.db, 'a') as file: # Membuka file
            data = json.dumps(data) # Merubah datanya jadi string agar bisa diterima oleh file teks
            file.write(data) # Menuliskan ke dalam file pada akhir baris
            file.write("\n") # Membuat garis baru untuk turun ke bawah datanya
  
    # fungsi read untuk baca data dr db trus disimpen pke var bertipe data list (array)
    def read(self):
        data: list = []
        with open(self.db) as file: # Membuka file
            for line in file.readlines(): # Membaca isi data per baris dengan looping
                item = line.strip()  # Menghapus whitespace (spasi atau apapun itu di ujung kanan dan kiri)
                item = json.loads(item) # Mengubah string yang disimpan jadi dictionary
                data.append(item) # Menambahkan ke array

        return data # Mengembalikan data
    
    # fungsi ini untuk ambil data berdasarkan id. dikembalikan dalam bntuk dictionary krn kita pngen tau id itu ada di baris ke berapa alias baris ke berapa data itu disimpan
    def get_by_id(self, id: str):
        single_item: dict = None
        item_line = 0

        with open(self.db) as file: # Buka file
            for line in file.readlines(): # Baca isi data satu per satu
                item_line += 1
                item = line.strip() # Hapus whitespace
                item = json.loads(item) # Ubah string (teks per baris) jadi dictionary

                if item.get('id') == id:
                    single_item = item.copy() # Copy -> memindahkan isi variabel item ke dalam variabel data
                    break # Break supaya looping ga lanjut, soalnya kan dah ketemu line berapa datanya

        return {"line": item_line, "data": single_item} # Balikkan dalam bentuk dictionary
    
    def update(self, id:str, updated_data: dict):
        single_item: dict = self.get_by_id(id)

        if not single_item.get('data'):
            return False
        
        with open(self.db, 'r') as file: # Membuka database txt
            lines = file.readlines() # Membaca data secara keseluruhan disimpan pada array
            lines[single_item['line'] - 1] = json.dumps(updated_data) + '\n'

            with open(self.db, 'w') as file:
                file.writelines(lines) # Data disimpan kembali dan ditulis ulang

        return {"line": single_item.get('line'), "data": updated_data}
