owl_numbers = set()

for i in range(1, 100001):
    digit_sum = sum(int(d) for d in str(i))
    owl_numbers.add(i + digit_sum)

non_owl_numbers = [n for n in range(1, 100001) if n not in owl_numbers]

print(non_owl_numbers[:100])