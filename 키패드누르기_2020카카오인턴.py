#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def distance(x1,x2,y1,y2): # 거리 구하기 함수
    return (abs(x1-x2)+abs(y1-y2))

def state_L(xl,yl,xd,yd,ans): # 왼손 엄지손가락 사용
    xl,yl=xd,yd
    ans+='L'
    return xl,yl,ans

def state_R(xr,yr,xd,yd,ans): # 오른손 엄지손가락 사용
    xr,yr=xd,yd
    ans+='R'
    return xr,yr,ans

def solution(numbers, hand):
    answer = ''
    arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,0,11]]) # *은 10, #은 11
    xL,yL,xR,yR= 3, 0, 3, 2

    for i in range(len(numbers)):
        xD,yD=np.where(arr==numbers[i]) # 눌러야 할 숫자
        xD,yD=int(xD),int(yD)
        print('xd: ',xD,' yd: ',yD) # 확인용
        dis_L=distance(xL,xD,yL,yD) # 왼손 거리
        dis_R=distance(xR,xD,yR,yD) # 오른쪽 거리
        print('dis_L: ',dis_L,'dis_R: ',dis_R)
        if numbers[i] in [1,4,7]: # 1,4,7 일 때,
            xL,yL,answer=state_L(xL,yL,xD,yD,answer) # 왼손 엄지손가락
        elif numbers[i] in [3,6,9]: # 3,6,9 일 때,
            xR,yR,answer=state_R(xR,yR,xD,yD,answer) # 오른손 엄지손가락 
        elif numbers[i] in [2,5,8,0]:
            if dis_L < dis_R: # 왼손에 가까우면
                xL,yL,answer=state_L(xL,yL,xD,yD,answer)
            elif dis_L > dis_R: # 오른손에 가까우면
                xR,yR,answer=state_R(xR,yR,xD,yD,answer)
            else: # 거리 같음
                if hand=="left": # 왼손잡이
                    xL,yL,answer=state_L(xL,yL,xD,yD,answer)
                elif hand=="right": # 오른손 잡이
                    xR,yR,answer=state_R(xR,yR,xD,yD,answer)
                else:
                    print("error")
    print('--------answer-------: ',answer)

    return answer

