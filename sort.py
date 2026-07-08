def display(arr, low, high):
    print(arr)

# bubble sort


def bubbleSort(arr, low, high):
    for i in range(low, high, 1):
        for j in range(low, high - i, 1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        # print(f"Iteration {i+1}")
        # display(arr, low, high)

# insertion sort


def insertionSort(arr, low, high):
    ctr = 0

    for i in range(low + 1, high + 1):
        j = i
        swapped = False

        while j > low and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            swapped = True

        ctr += 1
        # print(f"Iteration {ctr}")

        # if swapped:
        #     display(arr, low, high)

# heap sort


def heapify(arr, n, i):
    """
    Maintain Max Heap property for subtree rooted at index i.
    n = size of heap
    """

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Left child
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Right child
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # print(f"Heapify at index {i}")
        # display(arr, 0, n - 1)

        heapify(arr, n, largest)


def heapSort(arr, low, high):

    n = high - low + 1

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # print("\nMax Heap Constructed:")
    # display(arr, 0, n - 1)

    # Extract elements one by one
    iteration = 1
    for i in range(n - 1, 0, -1):

        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]

        # print(f"\nIteration {iteration}")
        # print(f"Placed maximum element at index {i}")

        # Heapify reduced heap
        heapify(arr, i, 0)

        # display(arr, 0, n - 1)

        iteration += 1


# quick sort (basic)


def partition(arr, low, high):
    # Lomuto partitioning, pivot is selected as the last element
    pivot = arr[high]
    x = low-1
    for i in range(low, high, 1):
        if (arr[i] < pivot):
            x += 1
            arr[x], arr[i] = arr[i], arr[x]
    arr[x+1], arr[high] = arr[high], arr[x+1]
    return x+1


def quickSort(arr, low, high):
    if (low < high):
        p = partition(arr, low, high)  # gives the index of the pivot element
        # print(f"Partition Element Index: {p}, Element: {arr[p]}")
        # print("Array after partitioning:")
        # display(arr, low, high)
        quickSort(arr, low, p-1)
        quickSort(arr, p+1, high)

# quicksort (advanced: 3-way partitioning)


def partition2(arr, low, high, pivot):
    # Dutch National Flag Algorithm
    lt = low
    gt = high
    i = low
    while i <= gt:
        if (arr[i] < pivot):
            arr[lt], arr[i] = arr[i], arr[lt]
            i += 1
            lt += 1
        elif (arr[i] > pivot):
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


def medianOThree(arr, low, high):
    mid = low+(high-low)//2

    if arr[low] > arr[mid]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if (arr[low] > arr[high]):
        arr[low], arr[high] = arr[high], arr[low]
    if (arr[mid] > arr[high]):
        arr[mid], arr[high] = arr[high], arr[mid]

    return arr[mid]


def quickSort2(arr, low, high):
    if (low < high):
        pivot = medianOThree(arr, low, high)
        # gives the index of the pivot element
        lt, gt = partition2(arr, low, high, pivot)
        # print("Array after partitioning:")
        # display(arr, low, high)
        quickSort2(arr, low, lt-1)
        quickSort2(arr, gt+1, high)

# mergesort (recursive)


def merge(arr, low, mid, high):
    # Create temporary arrays for the isolated sub-segments
    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    i = 0
    j = 0
    k = low
    len_left = len(left)
    len_right = len(right)

    # Merge elements back into arr[low...high] while elements remain in both sub-arrays
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Python Optimization: Replace manual copy loops with C-optimized slice assignments
    if i < len_left:
        arr[k:high+1] = left[i:]
    elif j < len_right:
        arr[k:high+1] = right[j:]


def mergeSort(arr, low, high):
    if low < high:
        mid = (low + high) // 2

        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)

        # print(f"Merging: [{low}...{mid}] and [{mid+1}...{high}]")
        merge(arr, low, mid, high)

        # print("Array after merging:")
        # display(arr, low, high)

# mergesort (iterative)


def mergeSort2(arr, low, high):
    # Determine the number of elements within the designated boundaries
    n = high - low + 1
    if n <= 1:
        return

    # Current size of subarrays to merge (doubles each pass: 1, 2, 4, 8, ...)
    curr_size = 1

    # Outer loop dictates the width of the sub-segments being merged
    while curr_size < n:

        # Inner loop picks the starting index of the left sub-array (anchored to low)
        left = low
        while left < high:

            # Calculate mid and right indices relative to the active 'left' anchor
            mid = left + curr_size - 1
            right = min(left + 2 * curr_size - 1, high)

            # Perform the merge operation only if a valid right sub-array exists
            if mid < right:
                merge(arr, left, mid, right)

            # Advance past both the left and right sub-arrays to process the next pair
            left += 2 * curr_size

        # Double the working sub-array size for the next hierarchical pass
        curr_size *= 2


# sieve sort


def sieveRecurse(seq):
    n = len(seq)
    if n <= 1:
        return list(seq)

    headers = []
    buckets = []

    for k in seq:
        placed = False

        if buckets and k < headers[0]:
            buckets[0].append(k)
            placed = True

        if not placed:
            for i in range(len(buckets)):
                if k == headers[i]:
                    headers.insert(i + 1, k)
                    buckets.insert(i + 1, [k])
                    placed = True
                    break
                if i + 1 < len(buckets):
                    if headers[i] < k < headers[i + 1]:
                        buckets[i + 1].append(k)
                        placed = True
                        break
                else:
                    headers.append(k)
                    buckets.append([k])
                    placed = True
                    break

        if not placed:
            headers.append(k)
            buckets.append([k])

    result = []
    for bucket in buckets:
        if len(bucket) == 1:
            result.extend(bucket)
        else:
            result.extend(sieveRecurse(bucket[::-1]))

    return result


def sieveSort(arr, low, high):
    n = high - low + 1
    if n <= 1:
        return

    sub = arr[low:high + 1]
    result = sieveRecurse(sub)

    for i in range(n):
        arr[low + i] = result[i]

# hrpsort


GAP = 5
THRESHOLD = 16


def medianOfMedians(arr, low, high):
    n = high - low + 1

    # Base case: if n is less than or equal to GAP, use insertion sort and return median
    if n <= GAP:
        insertionSort(arr, low, high)
        return arr[low + (n // 2)]

    # Step 1: Divide arr[low...high] into groups of GAP and find medians
    numOfMedians = 0
    for i in range(low, high + 1, GAP):
        subRight = i + GAP - 1
        if subRight > high:
            subRight = high  # Ensure subRight is within bounds

        # print(f"Sorting group A[{i}..{subRight}] using Insertion sort")
        insertionSort(arr, i, subRight)

        medianIdx = ((subRight - i + 1) // 2) + i
        arr[low + numOfMedians], arr[medianIdx] = arr[medianIdx], arr[low + numOfMedians]
        numOfMedians += 1
        # print(f"Sorting group A[{i}..{subRight}] after median swap")

        # display(arr, low, high)

    # print("Medians collected:", arr[low:low+numOfMedians])

    # Step 2: Recurse on the medians to find the pivot
    return medianOfMedians(arr, low, low + numOfMedians - 1)


def hrpSort(arr, low, high):
    n = high-low+1

    # print(f"\nhrpSort called on A[{low}..{high}]")

    if (n <= THRESHOLD):
        # print(f"Array size is less than {THRESHOLD}, sorting using Insertion Sort")
        insertionSort(arr, low, high)
        return

    # print(f"Array size is greater than {THRESHOLD}, entering HRP Sort")
    pivot = medianOfMedians(arr, low, high)
    # print("Pivot selected:", pivot)

    lt, gt = partition2(arr, low, high, pivot)  # 3-way partition algo

    leftPartitionSize = lt-low
    rightPartitionSize = high-gt

    if (leftPartitionSize < rightPartitionSize):
        # print("Sorting the smaller half using merge sort")
        mergeSort2(arr, low, lt-1)
        # print("After Merge Sort on smaller half:", arr)
        hrpSort(arr, gt+1, high)
    else:
        # print("Sorting the smaller half using merge sort")
        mergeSort2(arr, gt+1, high)
        # print("After Merge Sort on smaller half:", arr)
        hrpSort(arr, low, lt-1)


# amis sort

THRESHOLD2 = 32
MERGE_RATIO = 0.7
PIVOT_THRESHOLD = 1024


def choosePivot(arr, low, high):
    n = high - low + 1
    if n < PIVOT_THRESHOLD:
        return medianOThree(arr, low, high)
    return medianOfMedians(arr, low, high)


def amis(arr, low, high):
    while low < high:
        n = high - low + 1

        if n <= THRESHOLD2:
            insertionSort(arr, low, high)
            return

        pivot = choosePivot(arr, low, high)
        lt, gt = partition2(arr, low, high, pivot)

        leftSize = lt - low
        rightSize = high - gt

        if max(leftSize, rightSize) > 0:
            ratio = min(leftSize, rightSize) / max(leftSize, rightSize)
        else:
            ratio = 1.0

        if ratio < MERGE_RATIO:
            if leftSize < rightSize:
                if leftSize > 1:
                    mergeSort2(arr, low, lt - 1)
                low = gt + 1
            else:
                if rightSize > 1:
                    mergeSort2(arr, gt + 1, high)
                high = lt - 1
        else:
            if leftSize < rightSize:
                amis(arr, low, lt - 1)
                low = gt + 1
            else:
                amis(arr, gt + 1, high)
                high = lt - 1
