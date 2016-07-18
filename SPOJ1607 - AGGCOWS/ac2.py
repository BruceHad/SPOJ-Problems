from sys import stdin

def cows_fit(C, stalls, MIN):
	gaps = [stalls[i] - stalls[i-1] for i in range(1,len(stalls))]
	# First cow is fitted in the first stall
	stabled = 1
	
	# Subsequent cows are fitted in the next available stall with 
	# minimum distance
	distance, i = 0, 0
	for _ in range(C-1):
		while distance < MIN:
			if i > len(gaps) - 1: return False
			distance += gaps[i]
			i += 1
		stabled += 1
		distance = 0 # reset
		if(stabled == C): return True
	return False


def min_distance(C, stalls):
	stalls.sort()
	lo, hi = 1, stalls[-1]
	while lo <= hi:
		mid = lo + (hi-lo)/2
		fit = cows_fit(C, stalls, mid)
		if fit:
			lo = mid + 1
		else:
			hi = mid - 1
	if fit: return mid
	else: return mid - 1
	
no_of_cases = int(stdin.readline())

for i in range(no_of_cases):
	N, C = [int(x) for x in stdin.readline().split(' ')]
	stalls = []
	for i in range(N):
		stalls.append(int(stdin.readline()))
	print(min_distance(C, stalls))