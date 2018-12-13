df=pandas.read_csv('./input.txt', header=None)

total = df[0].sum()

print(total)