n = 3

line = ('* '*n).strip()

middle_line = [' ' for i in range(len(line))]
middle_line[0] = '*'
middle_line[-1] = '*'

middle_line = ''.join(middle_line)

print(line)
for i in range(n-2):
    print(middle_line)
print(line)