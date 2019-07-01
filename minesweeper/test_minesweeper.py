from minesweeper import Minesweeper


class TestMinesweeper:
    def test_empty_response(self):
        minesweeper = Minesweeper(0, 0)
        assert minesweeper.minesweeper() == (None, None), "expected none for empty grid"

    def test_empty_mine_list_response(self):
        minesweeper = Minesweeper(3, 2)
        assert minesweeper.minesweeper() == ([['.','.','.'],['.','.','.']], None), "expected empty grid for empty grid"

    def test_single_mine_response(self):
        minesweeper = Minesweeper(3, 2, [[0, 1]])
        assert minesweeper.minesweeper() == ([['.','*','.'],['.','.','.']], [['1','*','1'],['1','1','1']]), "expected empty grid for empty grid"

