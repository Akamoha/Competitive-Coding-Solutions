for _ in range(input()):
	N, M = map(int, raw_input().split())
	rowsHT = {}
	colsHT = {}
	A = []
	for n in range(N):
		A.append(map(int, raw_input().split()))
	for n in range(N):
		for m in range(M):
			if A[n][m] in rowsHT:
				if n in rowsHT[A[n][m]]:
					rowsHT[A[n][m]][n] += 1
				else:
					rowsHT[A[n][m]][n] = 1
			else:
				rowsHT[A[n][m]] = {}
				rowsHT[A[n][m]][n] = 1
			if A[n][m] in colsHT:
				if m in colsHT[A[n][m]]:
					colsHT[A[n][m]][m] += 1
				else:
					colsHT[A[n][m]][m] = 1
			else:
				colsHT[A[n][m]] = {}
				colsHT[A[n][m]][m] = 1
	
	m = 0
	for i in rowsHT:
		temp1 = max(rowsHT[i].values())
		temp2 = max(colsHT[i].values())
		mv = 0
		for mvkey_r, val in rowsHT[i].iteritems():
			if val == temp1:
				for mvkey_c, val2 in colsHT[i].iteritems():
					if val2 == temp2:
						if A[mvkey_r][mvkey_c] == i:
							mv = rowsHT[i][mvkey_r] + colsHT[i][mvkey_c] - 1
							if mv > m:
								m = mv
						else:
							mv = rowsHT[i][mvkey_r] + colsHT[i][mvkey_c]
							if mv > m:
								m = mv
							break
				else:
					continue
				break
	print m