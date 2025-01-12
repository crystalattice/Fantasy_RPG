from src.utils.dice_roller import multi_die


class TestSixSide:
    def test_1d6(self):
        for i in range(25):
            assert 1 <= multi_die(1, 1) <= 6

    def test_2d6(self):
        for i in range(25):
            assert 2 <= multi_die(2, 1) <= 12

    def test_3d6(self):
        for i in range(25):
            assert 3 <= multi_die(3, 1) <= 18

    def test_num_error(self):
        assert multi_die(0, 1) == 0
