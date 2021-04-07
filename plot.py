import matplotlib.pyplot as plt

with open('data/time.tsv', 'r') as f:
    data = f.read()

lines = data.split('\n')
timing = [line.split('\t') for line in lines]

func_names = set(item[0] for item in timing if item[0] != "")

time_dict = {}
for name in func_names:
    for t in timing:
        if t[0] == name:
            if name in time_dict.keys():
                time_dict[name].append(float(t[1]))
            else:
                time_dict[name] = [float(t[1])]

for func in time_dict.keys():
    plt.plot(
        [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000],
        time_dict[func], label=func
    )
plt.legend()
plt.ylim(top=20)
plt.show()
plt.savefig('data/benchmark.png')