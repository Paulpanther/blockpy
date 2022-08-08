def even():
    pass

colors = ['B', 'W', 'W', 'B', 'W', 'B', 'W']
n = len(colors)

bCount = 0
for color in colors:
    if color == 'B':
        bCount += 1

wCount = n - bCount

if (bCount % 2 == 1) and (wCount % 2 == 1):
    print("No")
else:
    moveW = wCount % 2 == 0

    for i in range(0, n - 1):
        color = colors[i]
        if color == 'W' and moveW:
            colors[i + 1] = 'W' if colors[i + 1] == 'B' else 'B'
            print(i)
        elif color == 'B' and not moveW:
            colors[i + 1] = 'W' if colors[i + 1] == 'B' else 'B'
            print(i)
