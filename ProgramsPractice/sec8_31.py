
text='python is a programming language'
# for p in text:
#     count=count+1
#     print(count)
#print(text.count('p'))
#using for loop
# ch='p'
# count=0
# for c in text:
#     if c==ch:
#         count+=1
# print(count)

#using dictionary
freq={}
for c in text:
    if c in freq:
        freq[c]+=1
    else:
        freq[c]=1
print(freq)