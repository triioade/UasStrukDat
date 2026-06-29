"""
tree_visualizer.py

Visualisasi Binary Search Tree
dalam bentuk ASCII console.
"""


class TreeVisualizer:

    def __init__(
        self,
        tree
    ):
        """
        menerima object BST
        """
        self.tree = tree



    # ==================================
    # PUBLIC METHOD
    # ==================================

    def tampilkan(self):
        print("\n")
        print("="*45)
        print(
            "        VISUALISASI BINARY SEARCH TREE"
        )

        print("="*45)


        if self.tree.root is None:
            print(
                "Tree masih kosong."
            )

        else:
            self._gambar_tree(
                self.tree.root,
                "",
                True
            )
        print("="*45)



    # ==================================
    # RECURSIVE DISPLAY
    # ==================================

    def _gambar_tree(
        self,
        node,
        prefix,
        is_left
    ):

        if node is not None:
            if node.right:
                self._gambar_tree(
                    node.right,
                    prefix +
                    ("│   " if is_left else "    "),
                    False
                )



            print(
                prefix +
                ("└── " if is_left else "┌── ")
                +
                str(node.data.id_buku)
            )



            if node.left:
                self._gambar_tree(
                    node.left,
                    prefix +
                    ("    " if is_left else "│   "),
                    True

                )