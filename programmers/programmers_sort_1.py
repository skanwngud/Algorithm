# k번째 수

def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i = commands[idx][0]-1
        j = commands[idx][1]
        k = commands[idx][2]-1

        if i == j:
            temp = list(array[i:i+1])
            temp = sorted(temp)
            print(idx, temp)
            temp = temp[k]
        elif i != j:
            temp = array[i:j]
            temp = sorted(temp)
            print(idx, temp)
            temp = temp[k]

        answer.append(temp)
    return answer