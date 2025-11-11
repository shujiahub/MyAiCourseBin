
def Binarysearch(nums,target):
    left = 0
    right= len(nums)-1

while left <= right:
    mid = (left + right)//2

    if target==nums[mid]:
       return mid
    
    if target<nums[mid] :
       left= mid-1
     else
        right= mid+1

return-1

nums=[2,7,11,15]
target=9
nums.sort()
print(Binarysearch(nums,target))