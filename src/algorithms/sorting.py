"""
sorting.py

Implementasi algoritma sorting manual.

Algoritma:
- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort
- Merge Sort
- Shell Sort
"""


class SortingEngine:
    """
    Class Sorting Engine.
    """
    # ======================================
    # BUBBLE SORT
    # ======================================
    def bubble_sort(self, data, key):
        """
        Bubble Sort
        Membandingkan dua data berdekatan.
        """
        data = data.copy()
        n = len(data)

        for i in range(n):
            for j in range(0, n - i - 1):
                if key(data[j]) > key(data[j + 1]):
                    data[j], data[j + 1] = (data[j + 1], data[j])

        return data

    # ======================================
    # INSERTION SORT
    # ======================================

    def insertion_sort(self, data, key):
        """
        Insertion Sort
        Menyisipkan data ke posisi benar.
        """

        data = data.copy()

        for i in range(1, len(data)):
            nilai = data[i]
            j = i - 1
            while j >= 0 and key(data[j]) > key(nilai):
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = nilai

        return data

    # ======================================
    # SELECTION SORT
    # ======================================

    def selection_sort(self, data, key):
        """
        Selection Sort
        Mencari nilai terkecil
        kemudian dipindahkan ke depan.
        """

        data = data.copy()
        n = len(data)

        for i in range(n):
            minimum = i
            for j in range(i + 1, n):
                if key(data[j]) < key(data[minimum]):
                    minimum = j
            data[i], data[minimum] = (data[minimum], data[i])
        return data

    # ======================================
    # QUICK SORT
    # ======================================

    def quick_sort(self, data, key):
        """
        Quick Sort menggunakan pivot.
        """
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        kiri = []
        tengah = []
        kanan = []

        for item in data:
            if key(item) < key(pivot):
                kiri.append(item)
            elif key(item) == key(pivot):
                tengah.append(item)
            else:
                kanan.append(item)

        return self.quick_sort(kiri, key) + tengah + self.quick_sort(kanan, key)

    # ======================================
    # MERGE SORT
    # ======================================

    def merge_sort(self, data, key):
        """
        Merge Sort.
        """
        if len(data) <= 1:
            return data
        tengah = len(data) // 2
        kiri = self.merge_sort(data[:tengah], key)
        kanan = self.merge_sort(data[tengah:], key)
        return self.merge(kiri, kanan, key)
    
    def merge(self, kiri, kanan, key):
        hasil = []
        i = 0
        j = 0

        while i < len(kiri) and j < len(kanan):
            if key(kiri[i]) <= key(kanan[j]):
                hasil.append(kiri[i])
                i += 1

            else:
                hasil.append(kanan[j])
                j += 1

        hasil.extend(kiri[i:])

        hasil.extend(kanan[j:])

        return hasil

    # ======================================
    # SHELL SORT
    # ======================================

    def shell_sort(self, data, key):
        """
        Shell Sort.
        Pengembangan dari insertion sort.
        """

        data = data.copy()
        n = len(data)

        jarak = n // 2

        while jarak > 0:
            for i in range(jarak, n):
                temp = data[i]
                j = i

                while j >= jarak and key(data[j - jarak]) > key(temp):
                    data[j] = data[j - jarak]
                    j -= jarak

                data[j] = temp
            jarak //= 2

        return data
