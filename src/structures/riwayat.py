"""
riwayat.py

Implementasi Double Linked List
untuk menyimpan riwayat aktivitas sistem.

Fitur:
- Tambah riwayat
- Tampilkan dari awal
- Tampilkan dari akhir
"""

from src.core.node import DoubleNode


class DoublyLinkedHistory:
    """
    Double Linked List Riwayat Aktivitas.
    """

    def __init__(self):

        # node pertama
        self.head = None

        # node terakhir
        self.tail = None

    # ======================================
    # TAMBAH RIWAYAT
    # ======================================

    def tambah_riwayat(self, aktivitas):
        """
        Menambahkan aktivitas baru
        ke bagian akhir list.
        """

        node_baru = DoubleNode(aktivitas)

        # jika list kosong
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru

        else:
            # hubungan node lama
            # dengan node baru
            self.tail.next = node_baru
            node_baru.prev = self.tail

            # update tail
            self.tail = node_baru

    # ======================================
    # TAMPIL MAJU
    # ======================================
    def tampil_maju(self):
        """
        Menampilkan riwayat
        dari aktivitas pertama.
        """
        if self.head is None:
            print("Belum ada riwayat.")
            return
        current = self.head

        print("\n===== RIWAYAT AKTIVITAS =====")

        nomor = 1
        while current:
            print(f"{nomor}. {current.data}")
            nomor += 1
            current = current.next

    # ======================================
    # TAMPIL MUNDUR
    # ======================================

    def tampil_mundur(self):
        """
        Menampilkan riwayat
        dari aktivitas terakhir.
        """
        if self.tail is None:
            print("Belum ada riwayat.")
            return
        current = self.tail

        print("\n===== RIWAYAT TERBARU =====")

        nomor = 1
        while current:
            print(f"{nomor}. {current.data}")
            nomor += 1
            current = current.prev

    # ======================================
    # HITUNG JUMLAH RIWAYAT
    # ======================================

    def jumlah_riwayat(self):
        """
        Menghitung jumlah aktivitas.
        """
        jumlah = 0
        current = self.head
        while current:
            jumlah += 1
            current = current.next
        return jumlah
