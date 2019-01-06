from unittest import TestCase
from Sorter import Sorter


class TestSorter(TestCase):
    def setUp(self):
        self.aa = Sorter([1, 4, 3, 2])

    def test_bubble_sort(self):
        rv = self.aa.bubbled_sort()
        self.assertEqual([1,2,3,4], rv)

    def test_sorted_(self):
        rv = self.aa.sorted_()
        self.assertEqual([1,2,3,4], rv)
