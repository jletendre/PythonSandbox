__all__ = ['Sorter']


class Sorter:
    def bubbled_sort(self) -> list:
        """
        Sorts a list using the bubble sort algorithm
        :rtype: object
        """
        if self.ori:
            temp = sorted(self.ori)
            # temp[1] = 10
            return temp
        return None

    def __init__(self, to_sort: list, sort_func=bubbled_sort):
        self.sort_func = sort_func
        self.ori = to_sort
        self.sorted_list = self.sort_func(self)

    def sorted_(self) -> list:
        return self.sorted_list

    def __repr__(self):
        return f'Sorter( {self.ori} )'


if __name__ == '__main__':
    my_sorter = Sorter([11, 4, 6, 2])

    my_sorted = my_sorter.sorted_()
    print(f"my_sorter:{my_sorter}")
    print(f"my_sorted:{my_sorted}")
