import re
index = [1,5,6,7,8,9,15,16,19]
print({i + 1: words[0] if i + 1 in index else words[:2] for i, words in enumerate(re.split(r'[, ]', 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'))})


