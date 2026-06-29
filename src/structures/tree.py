"""
tree.py

Implementasi Binary Search Tree (BST)

Digunakan untuk:
- Penyimpanan hierarki buku
- Pencarian berdasarkan ID buku
"""

from src.core.node import TreeNode


class BinarySearchTree:
    """
    Class Binary Search Tree.
    """

    def __init__(self):

        # root awal kosong
        self.root = None

    # ======================================
    # INSERT
    # ======================================

    def insert(self, buku):
        """
        Menambahkan buku ke BST.
        """

        node_baru = TreeNode(buku)

        if self.root is None:
            self.root = node_baru

        else:
            self._insert_recursive(self.root, node_baru)

    def _insert_recursive(self, current, node_baru):

        # masuk kiri

        if node_baru.data.id_buku < current.data.id_buku:
            if current.left is None:
                current.left = node_baru

            else:
                self._insert_recursive(current.left, node_baru)

        # masuk kanan

        else:
            if current.right is None:
                current.right = node_baru

            else:
                self._insert_recursive(current.right, node_baru)

    # ======================================
    # SEARCH
    # ======================================

    def search(self, id_buku):
        """
        Mencari buku berdasarkan ID.
        """
        return self._search_recursive(self.root, id_buku)

    def _search_recursive(self, current, id_buku):

        if current is None:
            return None

        if current.data.id_buku == id_buku:
            return current.data

        elif id_buku < current.data.id_buku:
            return self._search_recursive(current.left, id_buku)

        else:
            return self._search_recursive(current.right, id_buku)

    # ======================================
    # INORDER
    # ======================================

    def inorder(self):
        """
        Kiri - Root - Kanan
        Hasil otomatis urut ID.
        """

        print("\n===== BST INORDER =====")

        self._inorder_recursive(self.root)

    def _inorder_recursive(self, current):

        if current:
            self._inorder_recursive(current.left)

            print(current.data.id_buku, "-", current.data.judul)

            self._inorder_recursive(current.right)

    # ======================================
    # PREORDER
    # ======================================

    def preorder(self):
        """
        Root - Kiri - Kanan
        """

        print("\n===== BST PREORDER =====")

        self._preorder_recursive(self.root)

    def _preorder_recursive(self, current):

        if current:
            print(current.data.id_buku, "-", current.data.judul)

            self._preorder_recursive(current.left)
            self._preorder_recursive(current.right)

    # ======================================
    # POSTORDER
    # ======================================

    def postorder(self):
        """
        Kiri - Kanan - Root
        """
        print("\n===== BST POSTORDER =====")
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, current):

        if current:
            self._postorder_recursive(current.left)
            self._postorder_recursive(current.right)
            print(current.data.id_buku, "-", current.data.judul)
