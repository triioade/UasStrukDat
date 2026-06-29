"""
buku.py

Implementasi Single Linked List untuk
mengelola data buku perpustakaan.

Fitur:
- Tambah buku
- Hapus buku
- Tampilkan buku
- Cari buku
- Update buku
"""

from src.core.node import Node
from src.core.models import Buku


class LinkedListBuku:
    """
    Class Single Linked List Buku

    Setiap node menyimpan object Buku.
    """

    def __init__(self):
        # awal linked list kosong
        self.head = None

    # ======================================
    # TAMBAH BUKU
    # ======================================

    def tambah_buku(self, buku):
        """
        Menambahkan buku ke akhir linked list.
        """
        node_baru = Node(buku)

        # jika list masih kosong
        if self.head is None:
            self.head = node_baru

        else:
            current = self.head

            # menuju node terakhir
            while current.next:
                current = current.next

            # sambungkan node baru
            current.next = node_baru

    # ======================================
    # TAMPILKAN SEMUA BUKU
    # ======================================

    def tampilkan_buku(self):
        """
        Menampilkan seluruh data buku.
        """

        if self.head is None:
            print("\nData buku masih kosong.")
            return

        current = self.head

        print("\n===== DAFTAR BUKU =====")
        while current:
            print("------------------------")
            print(current.data.tampilkan_data())
            current = current.next

    # ======================================
    # HAPUS BUKU
    # ======================================

    def hapus_buku(self, id_buku):
        """
        Menghapus buku berdasarkan ID.
        """

        current = self.head
        previous = None

        while current:
            if current.data.id_buku == id_buku:
                # jika yang dihapus head
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                print("Buku berhasil dihapus.")

                return

            previous = current
            current = current.next

        print("Buku tidak ditemukan.")

    # ======================================
    # CARI BUKU
    # ======================================

    def cari_buku(self, id_buku):
        """
        Linear search sederhana pada Linked List.
        """

        current = self.head

        while current:
            if current.data.id_buku == id_buku:
                return current.data

            current = current.next

        return None

    # ======================================
    # UPDATE DATA BUKU
    # ======================================

    def update_buku(self, id_buku, judul, penulis, kategori, tahun):

        buku = self.cari_buku(id_buku)

        if buku:
            buku.judul = judul
            buku.penulis = penulis
            buku.kategori = kategori
            buku.tahun = tahun

            print("Data buku berhasil diperbarui.")

        else:
            print("Buku tidak ditemukan.")

    # ======================================
    # HITUNG JUMLAH BUKU
    # ======================================

    def jumlah_buku(self):
        """
        Menghitung jumlah node.
        Digunakan untuk laporan.
        """

        jumlah = 0
        current = self.head

        while current:
            jumlah += 1
            current = current.next

        return jumlah
