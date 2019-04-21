import time
import random

def insertion_sort(arr):
   for k in range(1,len(arr)):
     cur = arr[k]
     j = k
     while j>0 and arr[j-1]>cur:
         arr[j]=arr[j-1]
         j = j-1
     arr[j]=cur

def selection_sort(arr):
	for k in range(len(arr)):
		minimalindex = k
		j = k+1
		while j < len(arr):
			if arr[j] < arr[minimalindex]:
				minimalindex = j
			j = j+1
		temp = arr[k]
		arr[k] = arr[minimalindex]
		arr[minimalindex] = temp

if __name__ == '__main__':
	array_insertion = []; array_selection = []
	arraylength = [1000,2500,5000,7500,10000]
	for k in arraylength:
		array_insertion = []; array_selection = []
		for j in range(k):
			array_insertion.append(j)
			array_selection.append(j)
		start = time.clock()
		insertion_sort(array_insertion)
		end = time.clock()
		print(str(k) + ' ' + 'increasing' + ' ' + "insertion" + '{:.20f}'.format(end-start))
		start = time.clock()
		selection_sort(array_selection)
		end = time.clock()
		print(str(k) + ' ' + 'increasing' + ' ' + "selection" + '{:.20f}'.format(end-start))
		array_insertion = []; array_selection = []
		for j in range(k,0,-1):
			array_insertion.append(j)
			array_selection.append(j)
		start = time.clock()
		insertion_sort(array_insertion)
		end = time.clock()
		print(str(k) + ' ' + 'decreasing' + ' ' + "insertion" + '{:.20f}'.format(end-start))
		start = time.clock()
		selection_sort(array_selection)
		end = time.clock()
		print(str(k) + ' ' + 'decreasing' + ' ' + "selection" + '{:.20f}'.format(end-start))
		array_insertion = []; array_selection = []
		for j in range(k):
			rand = random.randint(0,99999)
			array_insertion.append(rand)
			array_selection.append(rand)
		start = time.clock()
		insertion_sort(array_insertion)
		end = time.clock()
		print(str(k) + ' ' + 'random' + ' ' + "insertion" + '{:.20f}'.format(end-start))
		start = time.clock()
		selection_sort(array_selection)
		end = time.clock()
		print(str(k) + ' ' + 'random' + ' ' + "selection" + '{:.20f}'.format(end-start))
	