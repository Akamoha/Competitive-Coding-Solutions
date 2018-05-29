n=input()
l=map(int, raw_input().split())
odd = False
if n%2 == 1:
	n += 1
	odd = True
	l.append(n)
d={}
ev=[]
od=[]
c=0
for i in l:
	d[i]=c
	c+=1
	if i&1:
		od.append(i)
	else:
		ev.append(i)
ev.sort()
od.sort()
pr=[]
for i in xrange(n/2):
	pr.append(od[i])
	pr.append(ev[i])
#print pr
c=0
for i in xrange(n):
	if pr[i]!=l[i]:
		z=d[pr[i]]
		tm=l[i]
		l[i]=l[z]
		l[z]=tm
		d[l[z]]=z
		c+=1
if not odd:
	if c%2 == 0:
		print "Petr"
	else:
		print "Um_nik"
else:
	if c%2 == 0:
		print "Um_nik"
	else:
		print "Petr"
	