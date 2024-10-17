files = ['a.txt', 'b.txt', 'c.txt']

for file in files:
    item = open(file, "r")
    content = item.read()
    print(content)
    item.close()