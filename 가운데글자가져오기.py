#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    answer = ''
    if len(s)>=1 and len(s)<=100:
        if len(s)%2==0:
            answer=s[int((len(s)/2)-1)]+s[(int(len(s)/2))]
            print('answer:[짝]',answer)
        else:
            answer=s[int(len(s)/2)]
            print('answer[홀]:',answer)
    return answer

