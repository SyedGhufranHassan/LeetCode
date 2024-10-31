def Duplicates(nums):
    #Find the unique elements from Nums
    unique=[nums[0]]
    for i in range(len(nums)):
        c=0
        for j in range(len(unique)):
            if nums[i] in unique:
                break
            else:
                unique.append(nums[i])
        
       
    #Find the count of unique elements  
    count=0  
    for k in range(len(unique)):
        count+=1
    
    #set the unique elements to the front of nums
    for i in range (count):
        nums[i]=unique[i]
        
    #find the count of remaining element and then pop them
    a=len(nums)-k
    for j in range(a-1):
        nums.pop()
        
    print(count)
    print(nums)


Duplicates([0,0,1,2,3,5,6,8,8,9,9])       
Duplicates([1,1,2,3,4,5,5,5])     
            
