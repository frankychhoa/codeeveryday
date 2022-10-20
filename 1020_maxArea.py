class Solution:
    def maxArea(self, height: List[int]) -> int:
        head,tail = 0, len(height)-1
        res=0
        
        while head < tail:
            h = min(height[head],height[tail])
            w = tail-head
            if h*w > res:
                res = h*w
            if height[tail] > height[head]:
                head += 1
            else:
                tail -= 1
        return res

# res=0
# arr=[height[0]]
# for i in range(1,len(height)):
#     #print(arr)
#     for j in range(len(arr)):
#         h = min([height[i],arr[j]])
#         width=i-j

#         if h*width > res:
#             res = h*width
#     arr.append(height[i])
    
# return res