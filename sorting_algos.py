# BUBBLE SORT
def bubble_sort(arr):
  for x in range(len(arr)):
    swapped = False
    for y in range(len(arr) - x - 1):
      if arr[y + 1] < arr[y]:
        swapped = True
        arr[y + 1], arr[y] = arr[y], arr[y + 1]
    if not swapped:
      break


# SELECTION SORT
def selection_sort(arr):
  for x in range(len(arr) - 1):
    minIndex = x
    for y in range(x + 1, len(arr)):
      if arr[y] < arr[minIndex]:
        minIndex = y
    if minIndex is not x:
      arr[x], arr[minIndex] = arr[minIndex], arr[x]


# INSERTION SORT
def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i - 1
    key = arr[j + 1]
    while j >= 0 and arr[j] > key:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key


# MERGE SORT
def merge(arr, l, m, r):
  n1 = m - l + 1
  n2 = r - m

  lArr = [None] * n1
  rArr = [None] * n2

  for i in range(n1):
    lArr[i] = arr[l + i]

  for i in range(n2):
    rArr[i] = arr[m + 1 + i]

  i = 0
  j = 0
  k = l

  while i < n1 and j < n2:
    if lArr[i] <= rArr[j]:
      arr[k] = lArr[i]
      i += 1
    else:
      arr[k] = rArr[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = lArr[i]
    i += 1
    k += 1

  while j < n2:
    arr[k] = rArr[j]
    j += 1
    k += 1


def merge_sort(arr, l, r):
  if (l >= r):
    return

  m = l + int((r - l) / 2)
  merge_sort(arr, l, m)
  merge_sort(arr, m + 1, r)
  merge(arr, l, m, r)


# QUICK SORT
def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1

  for j in range(low, high):
    if arr[j] < pivot:
      i += 1
      arr[j], arr[i] = arr[j], arr[i]

  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1


def quick_sort(arr, low, high):
  if low < high:
    pivot = partition(arr, low, high)
    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)


# HEAP SORT
def heapify(arr, n, i):
  largest = i

  l = 2 * i + 1
  r = 2 * i + 2

  if l < n and arr[l] > arr[largest]:
    largest = l

  if r < n and arr[r] > arr[largest]:
    largest = r

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    heapify(arr, n, largest)

def heap_sort(arr):
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify(arr, n, i)

  for i in range(n - 1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]
    heapify(arr, i, 0)