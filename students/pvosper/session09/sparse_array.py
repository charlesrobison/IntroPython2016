#!/usr/bin/env python3

'''
A spare array class should present to the user the same interface as a regular
list.

Some ideas of how to do that:

Internally, it can store the values in a dict, with the index as the keys. So
that only the indexes with non-zero values will be stored.

It should take a sequence of values as an initializer:


'''

class SparseArray:
    def __init__(self, seq):
        self.length = len(seq)
        self.sparse_dict = {}
        for i in range(len(seq)):
            if seq[i] > 0:
                self.sparse_dict[i] = seq[i]

    def __len__(self):
        return self.length
        
    def __getitem__(self, i):
        if i > self.length - 1:
            raise IndexError('list index out of range')
        elif i in self.sparse_dict.keys():
            return self.sparse_dict[i]
        else:
            return 0

    # This is crazy but works
    def __delitem__(self, i):
        if i > self.length - 1:
            raise IndexError('list index out of range')
        elif i in self.sparse_dict.keys():
            del self.sparse_dict[i]
            for j in self.sparse_dict.keys():
                if j > i:
                    self.sparse_dict[j - 1] = self.sparse_dict[j]
                    del self.sparse_dict[j]
            self.length -= 1
        else:
            for j in self.sparse_dict.keys():
                if j > i:
                    self.sparse_dict[j - 1] = self.sparse_dict[j]
                    del self.sparse_dict[j]
            self.length -= 1            

# sa = SparseArray([7,29,0,0,0,0,13,0,0,72])