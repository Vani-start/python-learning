


def BubbleSort(arr):
	n=len(arr)
	for i in range(n):
		print(i)
		for j in range(0,n-i-1):
			print(j)
			print(range(0,n-i-1))
			print(arr)
			if arr[j]>arr[j+1]:
				temp=arr[j]
				arr[j]=arr[j+1]
				arr[j+1]=temp
				print(arr)
			





arr=[21,12,34,67,13,9]
BubbleSort(arr)
print(arr)