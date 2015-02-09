import re
for _ in range(int(raw_input())):
    print "NO" if re.search("^[789][0-9]{9}$", raw_input()) == None else "YES"
