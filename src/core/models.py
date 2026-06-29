"""
models.py

Berisi class model/data utama pada
Sistem Perpustakaan Digital.

Class pada file ini hanya bertugas
menyimpan data, bukan mengatur struktur data.
"""


class Buku:
    """
    Class Buku digunakan untuk menyimpan
    informasi sebuah buku.

    Data buku nantinya akan digunakan oleh:
    - Single Linked List (Kelola Buku)
    - Binary Search Tree (Operasi Tree)
    - Searching Engine
    - Sorting Engine
    """

    def __init__(self, id_buku, judul, penulis, kategori, tahun):
        # Identitas buku
        self.id_buku = id_buku

        # Informasi buku
        self.judul = judul
        self.penulis = penulis
        self.kategori = kategori
        self.tahun = tahun

        # Status awal buku
        # Pilihan:
        # Tersedia
        # Dipinjam
        self.status = "Tersedia"

    def tampilkan_data(self):
        """
        Mengembalikan data buku dalam bentuk teks.
        Digunakan saat menampilkan daftar buku.
        """

        return (
            f"ID Buku     : {self.id_buku}\n"
            f"Judul       : {self.judul}\n"
            f"Penulis     : {self.penulis}\n"
            f"Kategori    : {self.kategori}\n"
            f"Tahun       : {self.tahun}\n"
            f"Status      : {self.status}"
        )

    def ubah_status(self, status_baru):
        """
        Mengubah status buku.

        Contoh:
        Tersedia -> Dipinjam
        Dipinjam -> Tersedia
        """

        self.status = status_baru
