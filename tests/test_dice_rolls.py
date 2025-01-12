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


class TestFourSide:
    def test_1d4(self):
        for i in range(25):
            assert 1 <= multi_die(1, 4) <= 4

    def test_2d4(self):
        for i in range(25):
            assert 2 <= multi_die(2, 4) <= 8

    def test_3d4(self):
        for i in range(25):
            assert 3 <= multi_die(3, 4) <= 16

    def test_num_error(self):
        assert multi_die(0, 1) == 0


class TestEightSide:
    def test_1d8(self):
        for i in range(25):
            assert 1 <= multi_die(1, 5) <= 8

    def test_2d8(self):
        for i in range(25):
            assert 2 <= multi_die(2, 5) <= 16

    def test_3d8(self):
        for i in range(25):
            assert 3 <= multi_die(3, 5) <= 24

    def test_num_error(self):
        assert multi_die(0, 1) == 0


class TestTenSide:
    def test_1d10(self):
        for i in range(25):
            assert 1 <= multi_die(1, 2) <= 10

    def test_2d10(self):
        for i in range(25):
            assert 2 <= multi_die(2, 2) <= 20

    def test_3d10(self):
        for i in range(25):
            assert 3 <= multi_die(3, 5) <= 30

    def test_num_error(self):
        assert multi_die(0, 1) == 0


class TestTwelveSide:
    def test_1d12(self):
        for i in range(25):
            assert 1 <= multi_die(1, 6) <= 12

    def test_2d12(self):
        for i in range(25):
            assert 2 <= multi_die(2, 6) <= 24

    def test_3d12(self):
        for i in range(25):
            assert 3 <= multi_die(3, 6) <= 36

    def test_num_error(self):
        assert multi_die(0, 1) == 0


class TestTwentySide:
    def test_1d20(self):
        for i in range(25):
            assert 1 <= multi_die(1, 7) <= 20

    def test_2d20(self):
        for i in range(25):
            assert 2 <= multi_die(2, 7) <= 40

    def test_3d20(self):
        for i in range(25):
            assert 3 <= multi_die(3, 7) <= 60

    def test_num_error(self):
        assert multi_die(0, 1) == 0


class TestPercentile:
    def test_1d100(self):
        for i in range(25):
            assert 1 <= multi_die(1, 3) <= 100

    def test_num_error(self):
        assert multi_die(0, 1) == 0
