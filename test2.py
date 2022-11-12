arr = [3,8,3,5,6,9,8,5,2,9,3,6,4,6,4,4,4,2,1,9,9,5,7,7,1,5,9,5,9,4,6,7,4,3,7,9,6,9,6,4,1,3,4,3,2,3,2,8,1,4,9,4,7,3,5]

def calculateMean (arr):
    print (sum(arr)/len(arr))

def calculateMode (arr):
    print(max(set(arr),key=arr.count))

def calculateMedian (arr):
    index =  int((len(arr) - 1)/2)
    arr = sorted(arr)
    print(index)
    if len(arr)%2 == 0:
        print(sorted(arr[index]))
    else:
        print(((arr[index]) + (arr[index + 1]))/2)

calculateMean(arr)
calculateMode(arr)
calculateMedian(arr)