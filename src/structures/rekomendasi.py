"""
rekomendasi.py

Implementasi Circular Doubly Linked List
untuk sistem rekomendasi buku.

Fitur:
- Tambah rekomendasi
- Generate rekomendasi berdasarkan kategori
- Hapus rekomendasi
- Tampilkan rekomendasi
- Navigasi next
- Navigasi previous
"""

from src.core.node import CircularDoubleNode


class CircularRecommendation:
    """
    Circular Doubly Linked List
    untuk menyimpan rekomendasi buku.
    """

    def __init__(self):

        # node awal
        self.head = None

        # node terakhir
        self.tail = None

        # posisi navigasi saat ini
        self.current = None


    # ======================================
    # TAMBAH REKOMENDASI
    # ======================================

    def tambah_rekomendasi(self, buku):
        """
        Menambahkan buku ke Circular Doubly Linked List.
        """

        node_baru = CircularDoubleNode(buku)


        # jika list kosong

        if self.head is None:

            self.head = node_baru
            self.tail = node_baru

            # membuat circular
            node_baru.next = node_baru
            node_baru.prev = node_baru


        else:

            # hubungan node baru

            node_baru.prev = self.tail
            node_baru.next = self.head

            self.tail.next = node_baru
            self.head.prev = node_baru


            # update tail

            self.tail = node_baru


        self.current = self.head



    # ======================================
    # GENERATE REKOMENDASI
    # ======================================

    def buat_rekomendasi(self, buku_target, daftar_buku):
        """
        Membuat rekomendasi berdasarkan kategori buku.

        Contoh:
        Buku kategori Pemrograman
        akan merekomendasikan buku lain
        dengan kategori Pemrograman.
        """


        # hapus rekomendasi lama

        self.clear()



        current = daftar_buku.head


        while current:


            buku = current.data


            # kategori sama
            # tetapi bukan buku yang dipilih

            if (
                buku.id_buku != buku_target.id_buku
                and
                buku.kategori == buku_target.kategori
            ):


                self.tambah_rekomendasi(
                    buku
                )


            current = current.next



    # ======================================
    # CLEAR DATA
    # ======================================

    def clear(self):
        """
        Menghapus seluruh isi rekomendasi.
        """

        self.head = None
        self.tail = None
        self.current = None



    # ======================================
    # TAMPIL REKOMENDASI
    # ======================================

    def tampilkan(self):
        """
        Menampilkan semua rekomendasi.
        """

        if self.head is None:

            print(
                "Belum ada rekomendasi."
            )

            return



        current = self.head


        print(
            "\n===== REKOMENDASI BUKU ====="
        )


        nomor = 1


        while True:


            buku = current.data


            print(
                f"{nomor}. {buku.judul}"
            )

            print(
                f"ID      : {buku.id_buku}"
            )

            print(
                f"Penulis : {buku.penulis}"
            )

            print(
                f"Kategori: {buku.kategori}"
            )

            print(
                f"Tahun   : {buku.tahun}"
            )

            print(
                "----------------------"
            )


            nomor += 1


            current = current.next



            if current == self.head:
                break



    # ======================================
    # NEXT BUKU
    # ======================================

    def next_buku(self):
        """
        Bergerak ke rekomendasi berikutnya.
        """

        if self.current is None:

            print(
                "Tidak ada rekomendasi."
            )

            return None



        self.current = self.current.next


        return self.current.data



    # ======================================
    # PREVIOUS BUKU
    # ======================================

    def previous_buku(self):
        """
        Bergerak ke rekomendasi sebelumnya.
        """

        if self.current is None:

            print(
                "Tidak ada rekomendasi."
            )

            return None



        self.current = self.current.prev


        return self.current.data



    # ======================================
    # HAPUS REKOMENDASI
    # ======================================

    def hapus_rekomendasi(self, id_buku):
        """
        Menghapus buku rekomendasi berdasarkan ID.
        """

        if self.head is None:

            print(
                "Rekomendasi kosong."
            )

            return



        current = self.head



        while True:


            if current.data.id_buku == id_buku:



                # jika hanya satu node

                if (
                    current == self.head
                    and
                    current == self.tail
                ):

                    self.head = None
                    self.tail = None
                    self.current = None



                else:


                    current.prev.next = current.next
                    current.next.prev = current.prev



                    if current == self.head:

                        self.head = current.next



                    if current == self.tail:

                        self.tail = current.prev

                print(
                    "Rekomendasi berhasil dihapus."
                )

                return
            current = current.next
            if current == self.head:
                break
        print(
            "Buku tidak ditemukan."
        )