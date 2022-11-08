#https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0),2:(0,1),3:(0,2),
              4:(1,0), 5:(1,1), 6:(1,2),
              7:(2,0),8:(2,1), 9:(2,2),
             '*':(3,0),0:(3,1),'#':(3,2)}
    left_hand_loc = keypad['*']
    right_hand_loc = keypad['#']
    for i in numbers:
        if i in [1,4,7]:
            answer +='L'
            left_hand_loc = keypad[i]
            
        elif i in [3,6,9]:
            answer += 'R'
            right_hand_loc = keypad[i]
            
        else:
            next_pad  = keypad[i]
            left_dis  = 0
            right_dis = 0
            left_dis  =  abs(left_hand_loc[0] - next_pad[0]) + abs(left_hand_loc[1] - next_pad[1])
            right_dis =  abs(right_hand_loc[0] - next_pad[0]) + abs(right_hand_loc[1] - next_pad[1])
            if left_dis < right_dis:
                answer += "L"
                left_hand_loc = next_pad
                
            elif left_dis > right_dis:
                answer += "R"
                right_hand_loc = next_pad
                
            else:
                if hand =="right":
                    answer +="R"
                    right_hand_loc = next_pad
                    
                else:
                    answer +="L"
                    left_hand_loc = next_pad
                    
            
            
    return answer