n = input()
k = input()
candies = [input() for _ in range(0,n)]
candies.sort()
i = 0
min_diff = candies[k-1] - candies[0]
l = len(candies)
while i + k < l:
    if min_diff > (candies[i+k-1] - candies[i]):
        min_diff = (candies[i+k-1] - candies[i])
    i += 1
print min_diff