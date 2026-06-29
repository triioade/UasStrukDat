"""
favorit.py

Implementasi Circular Singly Linked List
untuk menyimpan daftar buku favorit.

Fitur:
- Tambah buku favorit
- Hapus buku favorit
- Tampilkan buku favorit
"""

from src.core.node import CircularNode


class CircularFavorite:
    """
    Circular Singly Linked List Buku Favorit.
    """

    def __init__(self):

        # node awal
        self.head = None

        # node terakhir
        self.tail = None

    # ======================================
    # TAMBAH FAVORIT
    # ======================================

    def tambah_favorit(self, buku):
        """
        Menambahkan buku ke daftar favorit.
        """

        node_baru = CircularNode(buku)

        # jika masih kosong
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru

            # membuat circular

            self.tail.next = self.head

        else:
            # node terakhir menunjuk
            # ke node baru
            self.tail.next = node_baru
            self.tail = node_baru

            # kembali ke head

            self.tail.next = self.head
        print("Buku berhasil ditambahkan ke favorit.")

    # ======================================
    # HAPUS FAVORIT
    # ======================================

    def hapus_favorit(self, id_buku):
        """
        Menghapus buku favorit berdasarkan ID.
        """
        if self.head is None:
            print("Favorit masih kosong.")
            return

        current = self.head
        previous = self.tail

        while True:
            if current.data.id_buku == id_buku:
                # jika hanya satu data
                if self.head == self.tail:
                    self.head = None
                    self.tail = None

                # jika hapus head
                elif current == self.head:
                    self.head = self.head.next
                    self.tail.next = self.head

                # jika hapus tail

                elif current == self.tail:
                    self.tail = previous
                    self.tail.next = self.head

                else:
                    previous.next = current.next

                print("Buku favorit berhasil dihapus.")

                return

            previous = current
            current = current.next

            # kembali ke awal
            if current == self.head:
                break

        print("Buku tidak ditemukan.")

    # ======================================
    # TAMPIL FAVORIT
    # ======================================

    def tampil_favorit(self):
        """
        Menampilkan seluruh buku favorit.
        """

        if self.head is None:
            print("Belum ada buku favorit.")
            return
        current = self.head

        print("\n===== DAFTAR BUKU FAVORIT =====")

        nomor = 1

        while True:
            buku = current.data

            print(f"\n{nomor}. {buku.judul}")
            print(f"Penulis : {buku.penulis}")
            print(f"Tahun   : {buku.tahun}")
            nomor += 1
            current = current.next
            if current == self.head:
                break

    # ======================================
    # CEK KOSONG
    # ======================================

    def kosong(self):
        return self.head is None
