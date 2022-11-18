from collections import Counter

cnt = Counter()

for word in [1,2,3,3,3,4,4,4,4,3,2,4,4,2]:

    cnt[word] += 1

print(cnt[4])