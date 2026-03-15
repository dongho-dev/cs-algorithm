from collections import deque
import sys

dq = deque()

N = int(input())
for x in range(0, N):
    x = list(map(int, sys.stdin.readline().split()))

    if x[0] == 1:
        if (len(x) > 1):
            dq.append(x[1])
            
    elif x[0] == 2:  
        if (len(x) > 1):
            dq.appendleft(x[1])
            
    elif x[0] == 3: 
        if (len(dq) > 0):
            print(dq.pop())
        else:
            print(-1)    
            
    elif x[0] == 4:
        if (len(dq) > 0):
            print(dq.popleft())
        else:
            print(-1)  
        
    elif x[0] == 5: 
        print(len(dq))
        
    elif x[0] == 6: 
        if (len(dq) > 0):
            print(0)
        else:
            print(1)    
                    
    elif x[0] == 7: 
        if (len(dq) > 0):
            num = dq.pop()
            print(num)
            dq.append(num)
        else:
            print(-1)
        
    elif x[0] == 8:
        if (len(dq) > 0):
            num = dq.popleft()
            print(num)
            dq.appendleft(num)
        else:
            print(-1) 
        