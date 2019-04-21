def Josephus_problem(val,skip):
	arr = [None] * val
	skip = skip - 1
	for k in range(val):
		arr[k] = k + 1
	index = skip
	while len(arr) > 1:
		arr.pop(index)
		index = (index + skip) % len(arr)
	return arr

def Josephus2(val,skip):
	arr_1 = [None] * val
	arr_2 = []
	for k in range(val):
		arr_1[k] = k + 1
	index = skip-1
	while len(arr_1) >= skip:
		j = 0
		for k in range(index, len(arr_1), skip):
			arr_1[k] = None
			j = k
		index = (j + skip) % len(arr_1)
		for k in range(len(arr_1)):
			if arr_1[k] is not None:
				arr_2.append(arr_1[k])
		arr_1 = arr_2
		arr_2 = []
		index = index % len(arr_1)
	return arr_1

def Josephus(val,skip):
	arr = [None] * val
	for k in range(val):
		arr[k] = k+1
	return Josephus_helper(arr,0,skip)

def Josephus_helper(arr,index,skip):
	#if there's only one left, return that element
	count = 0
	target = 0
	for val in arr:
		if val is not None:
			count = count+1
			target = val
	if count == 1:
		return target

	#skip the specified times, None cell excluded
	current = index
	while skip != 1:
		if arr[(current+1)%len(arr)] is None:
			current = (current + 1) % len(arr)
		else:
			current = (current + 1) % len(arr)
			skip = skip - 1
	arr[current] = None

	#set the index at the first Non-None position
	current = (current + 1) % len(arr)
	while arr[current] is None:
		current = (current + 1) % len(arr)

	Josephus_helper(arr,current,skip)

def Josephus3(val,skip):
	arr = [None] * val
	for k in range(val):
		arr[k] = k + 1
	return Josephus3_helper(arr,skip,len(arr))

def Josephus3_helper(arr,skip,size):
	valid_size = size
	index = skip - 1
	while valid_size > 1:
		temp = arr[index]
		for k in range(index, valid_size-1):
			arr[k] = arr[k+1]
		arr[valid_size-1] = temp
		valid_size = valid_size - 1
		index = (index + skip -1) % valid_size
	return arr[0]





if __name__ == '__main__':
	print(Josephus_problem(41,3))
	print(Josephus2(41,2))
	print(Josephus(41,2))
	print(Josephus_helper([1,2,3,4,5,6,7],0,2))
	print(Josephus_helper([1,2,3,4,5],0,2))
	print(Josephus3(41,3))
