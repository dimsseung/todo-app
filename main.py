from app.todo import Todo
import os

todo = Todo()
while True:
    print("Selamat datang di aplikasi Todo")

    print("1. Tambah Todo")
    print("2. Lihat daftar Todo")
    print("3. Update status Todo")
    print("4. Hapus Todo")

    opsi = input("Masukkan pilihan anda: ")

    if opsi == "1":
        title = input("Masukkan judul todo: ")
        desc = input("Masukkan deskripsi todo: ")
        todo.create(title, desc)
        print("Berhasil menambahkan todo!")
        os.system("clear")
    elif opsi == "2":
        todo.read()
    elif opsi == "3":
        id = input("Masukkan ID Todo: ").strip()

        check_todo = todo.get_by_id(id)

        if not check_todo:
            continue