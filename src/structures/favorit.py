"""
favorit.py

Implementasi Circular Singly Linked List
untuk menyimpan buku favorit.

Fitur:
- Tambah buku favorit
- Hapus buku favorit
- Tampilkan buku favorit
"""

from src.core.node import CircularNode


class CircularFavorite:
    """
    Circular Singly Linked List
    untuk data buku favorit.
    """


    def __init__(self):

        # node pertama
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


        # kondisi jika kosong

        if self.head is None:


            self.head = node_baru
            self.tail = node_baru


            # membuat circular

            self.tail.next = self.head



        else:


            # tail menunjuk node baru

            self.tail.next = node_baru


            # update tail

            self.tail = node_baru


            # circular kembali ke head

            self.tail.next = self.head



        print(
            "Buku berhasil ditambahkan ke favorit."
        )



    # ======================================
    # TAMPIL FAVORIT
    # ======================================

    def tampilkan(self):
        """
        Menampilkan seluruh buku favorit.
        """


        if self.head is None:

            print(
                "Belum ada buku favorit."
            )

            return



        print(
            "\n===== DAFTAR BUKU FAVORIT ====="
        )



        current = self.head

        nomor = 1



        while True:


            buku = current.data



            print(
                f"{nomor}. {buku.judul}"
            )

            print(
                f"ID       : {buku.id_buku}"
            )

            print(
                f"Penulis  : {buku.penulis}"
            )

            print(
                f"Kategori : {buku.kategori}"
            )

            print(
                f"Tahun    : {buku.tahun}"
            )

            print(
                f"Status   : {buku.status}"
            )

            print(
                "----------------------------"
            )



            nomor += 1


            current = current.next



            # kembali ke head

            if current == self.head:

                break



    # ======================================
    # CARI FAVORIT
    # ======================================

    def cari_favorit(self, id_buku):
        """
        Mencari buku favorit berdasarkan ID.
        """


        if self.head is None:

            return None



        current = self.head



        while True:


            if current.data.id_buku == id_buku:

                return current.data



            current = current.next



            if current == self.head:

                break



        return None



    # ======================================
    # HAPUS FAVORIT
    # ======================================

    def hapus_favorit(self, id_buku):
        """
        Menghapus buku favorit berdasarkan ID.
        """


        if self.head is None:

            print(
                "Daftar favorit kosong."
            )

            return



        current = self.head

        previous = self.tail



        while True:



            if current.data.id_buku == id_buku:



                # jika hanya satu data

                if self.head == self.tail:


                    self.head = None
                    self.tail = None



                else:


                    previous.next = current.next



                    # hapus head

                    if current == self.head:

                        self.head = current.next



                    # hapus tail

                    if current == self.tail:

                        self.tail = previous



                    # menjaga circular

                    self.tail.next = self.head



                print(
                    "Buku berhasil dihapus dari favorit."
                )

                return



            previous = current

            current = current.next



            if current == self.head:

                break



        print(
            "Buku tidak ditemukan."
        )