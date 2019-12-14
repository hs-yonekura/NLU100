def make_ngram(arr: [], n: int):
    return list(tuple(arr[i:i + n]) for i in range(len(arr) + 1 - n))

print(make_ngram('I am an NLPer'.split(' '), 2))
print(make_ngram('I am an NLPer', 2))
