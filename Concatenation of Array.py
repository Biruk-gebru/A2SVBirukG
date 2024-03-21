ans=[]
i=0
while len(ans)<2*len(nums):
    if i==len(nums):
        i=0
    ans.append(nums[i])
    i+=1
return(ans)
