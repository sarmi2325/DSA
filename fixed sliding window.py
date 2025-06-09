arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4

window_start = 0
window_sum = 0
maxi=0
#sliding through window
for window_end in range(len(arr)):
    window_sum+=arr[window_end]
    
    if window_end>=k-1:
        maxi=max(window_sum,maxi)
        #moving forward one step by subtracting the current start element
        window_sum-=arr[window_start]
        window_start+=1
print(maxi)
