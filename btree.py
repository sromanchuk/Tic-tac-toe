from board import Board
from btnode import BTNode
import random


class BTree(BTNode, Board):
    """
    Class for binary tree representation.
    """
    def __init__(self, board=None):
        self._root = BTNode(board._board.copy())
        self._symbol = board._last_symbol
        self._size = 1

    def gen_board(self):
        """
        :return: generated board.
        """
        mass = self._root.data
        X_n = 0
        O_n = 0
        for i in range(len(mass)):
            if mass[i] == -10:
                X_n += 1
            elif mass[i] == 10:
                O_n += 1
        if X_n > O_n:
            sym = -10
        elif X_n == O_n:
            sym = 10

        indexes = []
        for i in range(len(mass)):
            if mass[i] != 10 and mass[i] != -10:
                indexes.append(i)
        cell = 0

        mass[random.choice(indexes)] = - sym
        sym = - sym
        board = Board(mass)
        board.draw_board()
        return mass

    def add_children(self):
        """
                Adds children to the binary tree.
                """
        def recurse1():
            pass
        # Helper function to search for item's position

        def recurse(node):
            mass = node.data
            board = Board(mass)
            result, finish = board.check_board()
            if finish:
                recurse(node.parent)
            else:
                if node.left == None:
                    print("Next left")
                    node.left = BTNode(node.gen_board(), parent=node)
                else:
                    if node.right == None:
                        print("Next right")
                        node.right = BTNode(node.gen_board(), parent=node)
                    else:
                        recurse(node.right)
                    recurse(node.left)

        recurse(self._root)
        self._size += 1
