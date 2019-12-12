# codeing: utf-8
import re
print([len(w) for w in re.sub(r'[\.,]', '', 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.').split(' ')
])
