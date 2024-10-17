filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for i in filenames:
    i = open(i, "w")
    i.write("Hello")
    i.close()