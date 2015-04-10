
def findMaxCrossingSubArray(A, low, mid, high):
    leftSum = -65536
    sum2 = 0
    maxLeft = 0
    
    for i in range(mid, low, -1):
        sum2 = sum2 + A[i]
        if sum2 > leftSum:
            leftSum = sum2
            maxLeft = i
    
    rightSum = -65536
    sum2 = 0
    maxRight = 0
    for j in range(mid+1, high):
        sum2 = sum2 + A[j]
        if sum2 > rightSum:
            rightSum = sum2
            maxRight = j
    return maxLeft, maxRight, leftSum + rightSum

def findMaximumSubArrary(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) / 2
        leftLow, leftHigh, leftSum = findMaximumSubArrary(A, low, mid)
        
        
        rightLow, rightHigh, rightSum = findMaximumSubArrary(A, mid + 1, high)
        
        crossLow, crossHigh, crossSum = findMaxCrossingSubArray(A, low, mid, high)
    
        if leftSum>=rightSum and leftSum>=crossSum:
            return leftLow, leftHigh, leftSum
        
        elif rightSum>=leftSum and rightSum>=crossSum:
            return rightLow, rightHigh, rightSum
        
        else:
            return crossLow, crossHigh, crossSum
        
        
if __name__ == '__main__':
    A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    low, high, sum2 = findMaximumSubArrary(A, 0, 15)
    print low, high, sum2
    
        
        
        
        
        
        
        
        