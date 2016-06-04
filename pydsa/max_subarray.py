#Time Complexity: O(n)
#Algorithmic Paradigm: Dynamic Programming
def max_subarray(A):
    """ 
    >>> from pydsa import max_subarray
    >>> list = [1, 2, 3, 5, -6, 4, 5]
    >>> max_subarray(list)
    14

    >>> list = [1,2,3,-7,2,3]
    >>> max_subarray(list)
    6

    """
	
    max_so_far = max_ending_here = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
       	max_so_far = max(max_so_far, max_ending_here)
    return max_so_far


