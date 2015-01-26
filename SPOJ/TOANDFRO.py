while True:
	N = int(raw_input())
	if N == 0:
		break
	else:
		s = raw_input()
		i = 0
		news = ""
		count = 0
		while count < len(s)/N:
			if count % 2 == 0:
				news += s[i:(i+N)]
			else:
				news += (s[i:(i+N)])[::-1]
			i += N
			count += 1
		
		i = 0
		newss = ""
		while i < N:
			j = i
			count = 0
			while count < len(s)/N:
				newss += news[j]
				count += 1
				j += N
			i += 1
			
		print newss