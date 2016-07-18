12/07/2016

http://www.spoj.com/problems/AGGRCOW/

# AGGRCOW - Aggressive cows

tags: binary-search

Farmer John has built a new long barn, with N (2 <= N <= 100,000) stalls. The stalls are located along a straight line at positions x1,...,xN (0 <= xi <= 1,000,000,000).

His C (2 <= C <= N) cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, FJ want to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?
Input

t – the number of test cases, then t test cases follows.
* Line 1: Two space-separated integers: N and C
* Lines 2..N+1: Line i+1 contains an integer stall location, xi
Output

For each test case output one integer: the largest minimum distance.
Example

Input:

1
5 3
1
2
8
4
9

Output:

3

Output details:

FJ can put his 3 cows in the stalls at positions 1, 4 and 8,
resulting in a minimum distance of 3.

## Notes

Tagged binary search so I guess that will need to be used, possibly to optimise a search of a fairly large data set (up to 100,000 stalls in up to 1,000,000,000 positions).

	>>> sys.maxint
	9223372036854775807

So ints should work fine here.

https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/

A binary search is one where the data set is cut in half on each check, making it very efficient for searching large sets O(log2).

	binary_search(A, target):
	   lo = 1, hi = size(A)
	   while lo <= hi:
		  mid = lo + (hi-lo)/2
		  if A[mid] == target:
			 return mid            
		  else if A[mid] < target: 
			 lo = mid+1
		  else:
			 hi = mid-1

We can reverse the questions and answer it fairly easily:

	for some minimum distance MIN we can determine the number of cows C that can fit in the stalls.

We can do this by first assigning the first cow to the first available stall and then searching for the next stall greater than MIN distance away. When we run out of stalls, then C is the number of cows in stalls.

But we need to reverse that somehow: For some number of cows C, what the best MIN distance that fits all the cows in stalls.


