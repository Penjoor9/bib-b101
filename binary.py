# binary serach
#inout array
arr = [3,4,5,6,7,8,9]
target = 9

low = 0
high = len(arr)-1#

#loop
while low < high:
    #divide
    mid = (low + high )
    # compare the middle with the target
    if arr[mid] == target:
        print('found')
        break
    #compare and discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1
