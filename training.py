def solution(number):
    num = []
    if number > 0:
        for i in range(1, number + 1):
            if i % 3 == 0:
                num.append(i)
            elif i % 5 == 0:
                num.append(i)
            
        return sum(num)
    
    else:
        return 0
    

print(solution(10))
#print(solution(4))
#print(solution(6))
#print(solution(16))
#print(solution(3))
#print(solution(5))
#print(solution(-1))
#print(solution(10))
#print(solution(20))
#print(solution(200))