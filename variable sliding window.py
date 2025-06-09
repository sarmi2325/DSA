#Longest Substring Without Repeating Characters
s="abcabcbb"

window_start=0
maxi=0
uniq=set()

for window_end in range(len(s)):
    while s[window_end] in uniq:
        uniq.remove(s[window_start])
        window_start+=1
    uniq.add(s[window_end])
    maxi=max(maxi,window_end-window_start+1)
    
print(maxi)
