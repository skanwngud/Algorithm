# 거리두기
# 5x5

# p = seat
# 0 = empty table
# x = line
# distance > 2

import numpy as np
def solution(places):
    answer = []
    for q in range(5):
        pla = []
        temp = places[q]
        person = []

        for x in range(5):
            for y in range(5):
                if temp[x][y] == "P":
                    person.append(np.array([x,y]))
                else:
                    continue

        for i in range(len(person)): 
            for j in range(len(person)):
                if np.abs(person[i]-person[j])[0]+np.abs(person[i]-person[j])[1] == 1:
                    pla.append("0")
                elif np.abs(person[i]-person[j])[0]+np.abs(person[i]-person[j])[1] == 2:
                    x_dif = np.abs(person[i]-person[j])[0]
                    y_dif = np.abs(person[i]-person[j])[1]
                    if x_dif == 2:
                        mid_x = int((person[i][0]+person[j][0])/2)
                        mid_y = person[i][1]
                        if temp[mid_x][mid_y]=="X":
                            pla.append("1")
                        else:
                            pla.append("0")
                    elif y_dif == 2:
                        mid_x = person[i][0]
                        mid_y = int((person[i][1]+person[j][1])/2)
                        if temp[mid_x][mid_y]=="X":
                            pla.append("1")
                        else:
                            pla.append("0")
                    else:
                        mid_1_x = person[i][0]
                        mid_1_y = person[j][1]
                        mid_2_x = person[j][0]
                        mid_2_y = person[i][1]
                        if temp[mid_1_x][mid_1_y]=="X" and temp[mid_2_x][mid_2_y]=="X":
                            pla.append('1')
                        else:
                            pla.append('0')

                else:
                    pla.append("1")
        if pla.count("0") != 0 :
            answer.append(0)
        else:
            answer.append(1)
        
    return answer