import re
# code1 = 'FVNISJND-XX-2020'
# code2 = 'FVNISJND-XY-2019'
# print(f'code1: {code1.endswith('2020')}')
# print(f'code2: {code2.endswith('2020')}')
#ends with
# code='ABC123'
# if re.search("123$",code):
#     print("ends with 123")

#starts with
path1 = 'youtube.com/watch?v=5EhRztVxums'
path2 = 'google.com/search?q=car'
print(f'code1: {path1.startswith('youtube')}')
print(f'code2: {path2.startswith('oogle')}')

if re.search("youtube",path1):
    print("starts with youtube...")