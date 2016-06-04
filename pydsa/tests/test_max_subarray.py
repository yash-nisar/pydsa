from pydsa.max_subarray import max_subarray

def test_max_subarray():
	assert max_subarray([1,-2,1,4,5,-10,3,5]) == 10
	assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
