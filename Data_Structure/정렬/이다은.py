'''
n = int(input()) # 1 <= n and n <= 1000000
num = []

for i in range(0, n):
    num.append(int(input()))

num.sort()

for j in range(0, n):
    print(num[j])
'''

# Merge Sort

# reference: https://m.blog.naver.com/PostView.nhn?blogId=bigbbbong&logNo=221251979668&proxyReferer=https%3A%2F%2Fwww.google.com%2Fhttps://m.blog.naver.com/PostView.nhn?blogId=bigbbbong&logNo=221251979668&proxyReferer=https%3A%2F%2Fwww.google.com%2F

def mergeSort(n):
    if len(n) <= 1:
        return n
    
    left = mergeSort(n[:len(n)//2])
    right = mergeSort(n[len(n)//2:])

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            n[k] = left[i]
            i += 1
        else:
            n[k] = right[j]
            j += 1
        k += 1
    
    if i == len(left):
        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1
    
    return n

N = int(input()) # 1 <= N and N <= 1000000
arr = []

for i in range(0, N):
    arr.append(int(input()))

arr = mergeSort(arr)

for j in range(0, N):
    print(arr[j])