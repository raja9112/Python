import heapq

def minComputation(size, files):
    # Create a priority queue
    # to store the size of the files
    heapq.heapify(files)

    # Variable to store the
    # total computations
    count = 0

    while(len(files) > 1):
        # pop two smallest
        # size files from heap
        temp = heapq.heappop(files) + heapq.heappop(files)

        # add the current computations
        # to the total computations
        count += temp

        # add the new combined file size
        # to priority queue or min heap
        heapq.heappush(files, temp)

    # return the minimum
    # computations required
    return count

# Driver code
if __name__ == "__main__":
    # no of files
    size = 5

    # 6 files with their sizes
    files = [ 20, 30, 5, 10, 30 ]

    # total no of computations
    # do be done final answer
    print("Minimum Computations = ", minComputation(size, files))
