string = raw_input()
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
countodd = 0
for x in string:
    count[ord(x)-96] = count[ord(x)-96] + 1

for x in range(0,26):
    if count[x] % 2 != 0:
        countodd = countodd + 1
        
if countodd == 0 and len(string) % 2 == 0:
    print("YES")
elif countodd == 1 and len(string) % 2 == 1:
    print("YES")
else:
    print("NO")