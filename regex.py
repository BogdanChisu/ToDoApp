import re

pin = "123d"
p = re.findall("\D", pin)
print(p)