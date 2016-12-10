class SparseArray():
    def __init__(self, arr):
        self.sa = {x: arr[x] for x in range(len(arr)) if arr[x] != 0}
        self._len = len(arr)

    def __call__(self, arr):
        return SparseArray(arr)

    def __len__(self):
        return self._len

    def __getitem__(self, ind):
        if ind < self._len:
            if ind in self.sa:
                return self.sa[ind]
            else:
                return 0
        else:
            return IndexError

    def __setitem__(self, key, value):
        if value != 0:
            self.sa[key] = value
        elif key in self.sa:
            del self.sa[key]
        if key >= self._len:
            self._len = key + 1

    def __str__(self):
        print_arr = "["
        for x in range(self._len):
            print_arr += str((self.__getitem__(x))) + ", "
        print_arr = print_arr[:-2] + "]"
        return print_arr

    def __contains__(self, query):
        return query in self.sa or (query == 0 and len(list(self.sa.keys())) < self._len)

    def __delitem__(self, key):
        if key in self.sa or key < self._len:
            # del self.sa[key]
            self.shift_keys(key)
            self._len -= 1
        else:
            return IndexError

    def append(self, num):
        if isinstance(num, int):
            self.sa[self._len] = num
            self._len += 1
        else:
            return TypeError

    def shift_keys(self, start):
        key_list = sorted(list(self.sa.keys()))
        if start in key_list:
            start_ind = key_list.index(start) + 1
            del self.sa[start]
        else:
            for x in key_list:
                if x > start:
                    start_ind = key_list.index(x)
                    break
        for x in key_list[start_ind:]:
            self.sa[x - 1] = self.sa[x]
        del self.sa[key_list[-1]]
