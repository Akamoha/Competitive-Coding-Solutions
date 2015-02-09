numLines = int(raw_input())
count = 0
for _ in range(numLines):
    line = raw_input()
    count += line.count('=')
print count
