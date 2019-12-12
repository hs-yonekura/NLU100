# coding: utf-8

from functools import reduce
target1 = 'パトカー'
target2 = 'タクシー'

print(''.join(reduce(lambda x, y: x + y, zip(target1, target2))))
