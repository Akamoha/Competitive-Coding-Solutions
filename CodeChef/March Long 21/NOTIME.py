def r(): return list(map(int, input().split()))
_,H,x = r()
print(['yes','no'][max(r())+x<H]) 