N, K = map(int, raw_input().split())
flowerPrices = map(int, raw_input().split())
flowerPrices.sort(reverse = True)
numBought = 0
cost = 0
iteration = 0
while numBought < N:
    for person in range(K):
        if numBought < N:
            cost += flowerPrices[numBought] * (iteration + 1)
            numBought += 1
        else:
            break
    iteration += 1
print cost