import re 

text = 'the quick brown box jumps over the lazy dog'

match = re.search('box',text)

if match:
    print('this is a found')
    print(match.start())
    print(match.end())
else:
    print('not found')


match = re.findall('the',text , re.IGNORECASE)
print(match)