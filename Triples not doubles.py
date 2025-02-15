res = []
i = 1
while len(res) < 50:
    if i % 3 == 0 and i % 2 != 0:
        res.append(i)
    i += 1
print(res)