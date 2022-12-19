lst = [int(input()) for i in range(9)]
answer = False
    
for i in range(8):
    if answer: #답이 이미 나온 경우
        break
        
    for j in range(i+1, 9):
        if sum(lst) - lst[i] - lst[j] == 100: #2명 뺸 7명의 합이 100인 경우
            lst.pop(i)
            lst.pop(j-1)
            
            for k in sorted(lst):
                print(k)
                
            answer = True #답이 나옴
            break
