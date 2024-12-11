import re

line = "Arizona 479, 501, 870. California 209, 213, 650."
m = re.findall("[0-9]+", line)
print(m)