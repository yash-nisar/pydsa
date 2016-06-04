def max_subarray(A):
    """        
The maximum subarray problem is the task of finding the contiguous 
subarray within a one-dimensional array of numbers which has the 
largest sum. For example, for the sequence of values
(-2, 1, -3, 4, -1, 2, 1, -5, 4), the contiguous subarray with 
the largest sum is [4, -1, 2, 1] with sum 6.
	
Time Complexity: O(n)
	
Algorithmic Paradigm: Dynamic Programming
	
Explanation:
Simple idea of the Kadane's algorithm is to look for all positive 
contiguous segments of the array (max_ending_here is used for this). 
And keep track of maximum sum contiguous segment among all positive 
segments (max_so_far is used for this). Each time we get a positive sum 
compare it with max_so_far and update max_so_far if it is greater 
than max_so_far
    """	
	
	
	
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
       	max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


