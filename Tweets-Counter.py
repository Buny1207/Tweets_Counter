from collections import Counter

lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = input()

    lst.append(ele)
lst

for i in lst:
    names = i.split()[0]

    names

ls = []

for i in lst:
    nm = i.split()[0]

    ls.append(nm)

    ls

times = Counter(ls)
rp = times.values()
max_v = max(times.values())

max_v

temp = []

for key, value in sorted(times.items()):

    if value == max_v:
        print(key, value)