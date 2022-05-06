#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(numbers):
    iter_n=len(numbers)-1
    k=iter_n
    total=[]
    for i in range(iter_n):
        for j in range(iter_n):
            x=numbers[i]+numbers[k-j]
            print('x1',numbers[i],'x2',numbers[k-j])
            if x in total:
                print('next')
            else:
                total.append(x)
                total.sort()
            
        iter_n=iter_n-1
    
    answer = total
    return answer

