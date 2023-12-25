# using inclusion / exclusion principle
three = []
five = []
fiveteen = []
for k in range(0, 1000, 3):
    three.append(k)
for k in range(0, 1000, 5):
    five.append(k)
for k in range(0, 1000, 15):
    fiveteen.append(k)

print(sum(three) + sum(five) - sum(fiveteen))
