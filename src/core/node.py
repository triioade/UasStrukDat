"""
node.py

Berisi seluruh implementasi Node manual
yang digunakan oleh struktur data pada
Sistem Perpustakaan Digital.

Struktur data yang membutuhkan Node:
- Single Linked List
- Queue
- Double Linked List
- Circular Linked List
- Binary Search Tree
"""


# ==========================================
# NODE UNTUK SINGLE LINKED LIST
# ==========================================


class Node:
    """
    Node dasar untuk Single Linked List.
    Digunakan pada:
    - Kelola Buku
    """
    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================
# NODE UNTUK QUEUE
# ==========================================


class QueueNode:
    """
    Node untuk struktur Queue FIFO.
    Digunakan pada:
    - Sistem Peminjaman
    """

    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================================
# NODE UNTUK DOUBLE LINKED LIST
# ==========================================


class DoubleNode:
    """
    Node untuk Double Linked List.
    Digunakan pada:
    - Riwayat Aktivitas
    """

    def __init__(self, data):
        self.data = data

        # menunjuk node sebelumnya
        self.prev = None

        # menunjuk node berikutnya
        self.next = None


# ==========================================
# NODE UNTUK CIRCULAR SINGLY LINKED LIST
# ==========================================


class CircularNode:
    """
    Node untuk Circular Singly Linked List.
    Digunakan pada:
    - Buku Favorit
    """

    def __init__(self, data):
        self.data = data

        # node berikutnya
        self.next = None


# ==========================================
# NODE UNTUK CIRCULAR DOUBLE LINKED LIST
# ==========================================


class CircularDoubleNode:
    """
    Node untuk Circular Doubly Linked List.
    Digunakan pada:
    - Sistem Rekomendasi Buku
    """

    def __init__(self, data):
        self.data = data

        # node sebelumnya
        self.prev = None

        # node berikutnya
        self.next = None


# ==========================================
# NODE UNTUK BINARY SEARCH TREE
# ==========================================


class TreeNode:
    """
    Node untuk Binary Search Tree.
    Digunakan pada:
    - Operasi Tree
    - Searching berdasarkan ID Buku
    """

    def __init__(self, data):
        self.data = data

        # cabang kiri
        self.left = None

        # cabang kanan
        self.right = None
