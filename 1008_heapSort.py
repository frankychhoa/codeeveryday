class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def max_heapify(heap_size,index):
            left, right = index*2+1, index*2+2
            largest=index
            if left < heap_size and nums[left]>nums[largest]:
                largest=left
            if right < heap_size and nums[right]>nums[largest]:
                largest=right
            if largest != index:
                temp=nums[largest]
                nums[largest], nums[index]= nums[index],temp
                max_heapify(heap_size,largest)
        
        for i in range(len(nums)//2,-1,-1):
            max_heapify(len(nums),i)
        
        
        for i in range(len(nums)-1,0,-1):
            #print(nums)
            #swap
            temp=nums[i]
            nums[i],nums[0] = nums[0],temp
            max_heapify(i,0)
        return nums