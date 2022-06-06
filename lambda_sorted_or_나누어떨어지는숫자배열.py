#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(arr, divisor):
    if len(arr) > 0:
        l=list(filter(lambda arr:arr%divisor==0,arr))
        if len(l)==0:
            l=[-1]
        else:
            l.sort()
    return l

