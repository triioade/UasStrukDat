"""
main.py

Program utama:
Sistem Perpustakaan Digital

Mengatur:
- Menu utama
- Interaksi user
- Integrasi semua struktur data
"""

from src.core.models import Buku
from src.structures.buku import LinkedListBuku
from src.structures.peminjaman import QueuePeminjaman
from src.structures.riwayat import DoublyLinkedHistory
from src.structures.favorit import CircularFavorite
from src.structures.rekomendasi import CircularRecommendation
from src.structures.tree import BinarySearchTree
from src.algorithms.searching import SearchingEngine
from src.algorithms.sorting import SortingEngine
from src.reports.laporan import LaporanSistem
from src.services.json_manager import JSONManager
from src.services.analytics import Analytics
from src.services.tree_visualizer import TreeVisualizer


# ==========================================
# INISIALISASI SISTEM
# ==========================================


daftar_buku = LinkedListBuku()
antrian_pinjam = QueuePeminjaman()
riwayat = DoublyLinkedHistory()
favorit = CircularFavorite()
rekomendasi = CircularRecommendation()
tree = BinarySearchTree()
search = SearchingEngine()
sorting = SortingEngine()
json_manager = JSONManager()
analytics = Analytics(daftar_buku)
tree_visualizer = TreeVisualizer(tree)


# ==========================================
# KONVERSI LINKED LIST KE LIST
# Untuk Searching & Sorting
# ==========================================


def ambil_semua_buku():
    data = []
    current = daftar_buku.head

    while current:
        data.append(current.data)
        current = current.next

    return data


# ==========================================
# MENU KELOLA BUKU
# ==========================================


def menu_buku():

    while True:
        print("\n===== KELOLA BUKU =====")
        print("1. Tambah Buku")
        print("2. Hapus Buku")
        print("3. Tampilkan Buku")
        print("0. Kembali")

        pilihan = input("Pilih : ")

        if pilihan == "1":
            id_buku = int(input("ID Buku : "))
            judul = input("Judul : ")
            penulis = input("Penulis : ")
            kategori = input("Kategori : ")
            tahun = int(input("Tahun : "))
            buku = Buku(id_buku, judul, penulis, kategori, tahun)
            daftar_buku.tambah_buku(buku)
            tree.insert(buku)
            riwayat.tambah_riwayat(f"Menambahkan buku {judul}")

            print("Buku berhasil ditambahkan.")

        elif pilihan == "2":
            id_buku = int(input("ID Buku : "))
            daftar_buku.hapus_buku(id_buku)
            riwayat.tambah_riwayat(f"Menghapus buku ID {id_buku}")

        elif pilihan == "3":
            daftar_buku.tampilkan_buku()

        elif pilihan == "0":
            break


# ==========================================
# MENU PEMINJAMAN
# ==========================================


def menu_peminjaman():

    print("\n===== PEMINJAMAN =====")
    nama = input("Nama peminjam : ")
    id_buku = int(input("ID Buku : "))
    buku = daftar_buku.cari_buku(id_buku)

    if buku:
        if buku.status == "Tersedia":
            data = f"{nama} meminjam {buku.judul}"
            antrian_pinjam.tambah_antrian(data)
            buku.status = "Dipinjam"
            riwayat.tambah_riwayat(data)

        else:
            print("Buku sedang dipinjam.")

    else:
        print("Buku tidak ditemukan.")


# ==========================================
# MENU PENGEMBALIAN
# ==========================================


def menu_pengembalian():

    print("\n===== PENGEMBALIAN =====")
    id_buku = int(input("ID Buku : "))
    buku = daftar_buku.cari_buku(id_buku)

    if buku:
        buku.status = "Tersedia"
        aktivitas = f"Buku {buku.judul} dikembalikan"
        riwayat.tambah_riwayat(aktivitas)
        print("Pengembalian berhasil.")

    else:
        print("Buku tidak ditemukan.")


# ==========================================
# MENU SEARCHING
# ==========================================


def menu_searching():

    data = ambil_semua_buku()

    while True:
        print("\n===== SEARCHING ENGINE =====")
        print("1. Search by Name (Linear Search)")
        print("2. Search by ID (Binary Search)")
        print("0. Kembali")

        pilihan = input("Pilih metode : ")

        # ==============================
        # SEARCH JUDUL
        # ==============================

        if pilihan == "1":
            nama = input("Masukkan nama/judul buku : ")
            hasil = search.linear_search_name(data, nama)

            if hasil:
                print("\n===== HASIL PENCARIAN =====")
                for buku in hasil:
                    print(buku.tampilkan_data())

                    print("------------------")

            else:
                print("Buku tidak ditemukan.")

        # ==============================
        # SEARCH ID
        # ==============================

        elif pilihan == "2":
            id_buku = int(input("Masukkan ID Buku : "))

            # Binary Search membutuhkan data urut
            data_urut = sorting.merge_sort(data, lambda x: x.id_buku)
            hasil = search.binary_search_id(data_urut, id_buku)

            if hasil:
                print("\nBuku ditemukan:")
                print(hasil.tampilkan_data())

            else:
                print("Buku tidak ditemukan.")

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# MENU SORTING
# ==========================================


def menu_sorting():

    data = ambil_semua_buku()
    print("\n1. Bubble")
    print("2. Insertion")
    print("3. Selection")
    print("4. Quick")
    print("5. Merge")
    print("6. Shell")

    pilih = input("Metode : ")

    metode = {
        "1": sorting.bubble_sort,
        "2": sorting.insertion_sort,
        "3": sorting.selection_sort,
        "4": sorting.quick_sort,
        "5": sorting.merge_sort,
        "6": sorting.shell_sort,
    }

    hasil = metode[pilih](data, lambda x: x.id_buku)

    print("\n===== HASIL SORTING =====")

    for buku in hasil:
        print(buku.id_buku, "-", buku.judul)


# ==========================================
# MENU TREE
# ==========================================


def menu_tree():

    print("\n===== OPERASI TREE =====")
    print("1. Inorder")
    print("2. Preorder")
    print("3. Postorder")
    print("4. Cari Buku")

    pilih = input("Pilih : ")

    if pilih == "1":
        tree.inorder()

    elif pilih == "2":
        tree.preorder()

    elif pilih == "3":
        tree.postorder()

    elif pilih == "4":
        id_buku = int(input("ID Buku : "))

        hasil = tree.search(id_buku)

        if hasil:
            print(hasil.tampilkan_data())

        else:
            print("Tidak ditemukan.")


# ==========================================
# MENU FITUR TAMBAHAN
# ==========================================


def menu_tambahan():

    while True:
        print("\n===== FITUR TAMBAHAN =====")
        print("1. Simpan Data JSON")
        print("2. Muat Data JSON")
        print("3. Statistik Perpustakaan")
        print("4. Visualisasi BST")
        print("0. Kembali")

        pilihan = input("Pilih : ")

        # ==============================
        # SIMPAN DATA JSON
        # ==============================

        if pilihan == "1":
            nama_file = input("Nama file (tanpa .json) : ")
            data = ambil_semua_buku()
            json_manager.save_json(nama_file, data)

        # ==============================
        # MUAT DATA JSON
        # ==============================

        elif pilihan == "2":
            nama_file = input("Nama file (tanpa .json) : ")
            data = ambil_semua_buku()
            buku_baru = json_manager.load_json(nama_file, data)

            # Tambahkan buku baru ke sistem
            for buku in buku_baru:
                daftar_buku.tambah_buku(buku)
                tree.insert(buku)
                riwayat.tambah_riwayat(f"Memuatkan buku {buku.judul} dari JSON")

            if buku_baru:
                print(f"\n{len(buku_baru)} buku berhasil dimuat.")

        # ==============================
        # STATISTIK PERPUSTAKAAN
        # ==============================

        elif pilihan == "3":
            analytics.tampilkan_dashboard()

        # ==============================
        # VISUALISASI BST
        # ==============================

        elif pilihan == "4":
            tree_visualizer.tampilkan()

        elif pilihan == "0":
            break

        else:
            print("Pilihan tidak tersedia.")


# ==========================================
# PROGRAM UTAMA
# ==========================================


def main():

    while True:
        print("\n")
        print("=" * 40)

        print(" SISTEM PERPUSTAKAAN DIGITAL ")

        print("=" * 40)

        print(
            """
[1] Kelola Buku
[2] Peminjaman
[3] Pengembalian
[4] Searching Engine
[5] Sorting Engine
[6] Operasi Tree
[7] Laporan Sistem
[8] Fitur Tambahan
[0] Keluar
"""
        )

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            menu_buku()
        elif pilihan == "2":
            menu_peminjaman()
        elif pilihan == "3":
            menu_pengembalian()
        elif pilihan == "4":
            menu_searching()
        elif pilihan == "5":
            menu_sorting()
        elif pilihan == "6":
            menu_tree()

        elif pilihan == "7":
            laporan = LaporanSistem(daftar_buku, riwayat, favorit, rekomendasi)
            laporan.tampilkan_laporan()

        elif pilihan == "8":
            menu_tambahan()

        elif pilihan == "0":
            print("Program selesai.")

            break

        else:
            print("Menu tidak tersedia.")


# menjalankan program

main()
