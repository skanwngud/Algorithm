# 아이디

# 본인 풀이
new_id = "...!@BaT#*..y.abcdefghijklm"
new_id_2 = '=.='
new_id_3 = '123_.def'
new_id_4 = "abcdefghijklmn.p"

def solution(new_id):
    id = list()

    # 1 단계
    answer = new_id.lower()
    answer = list(answer)
    print('step 1 : ', answer)

    # 2 단계
    for i in range(len(answer)):
        if answer[i].islower() == True:
            id.append(answer[i])
        else :
            if answer[i] in ['-', '_', '.']:
                id.append(answer[i])
            elif answer[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                id.append(answer[i])

    id = ''.join(id)

    print('step 2 : ', id)

    # 3 단계
    while '..' in id:
        id = id.replace('..', '.')
            
    print('step 3 : ', id)

    # 4 단계
    if id[0] == '.':
        id = id[1:]
    elif id[-1] == '.':
        id = id[:-1]

    print('step 4 : ', id)

    # 5 단계
    if id == '':
        id = 'a'*3

    # 6 단계
    if len(id) > 15:
        id = id[:15]
        if id[-1] == '.':
            id = id[:-1]

    print('step 6 : ', id)

    # 7 단계
    if len(id) < 3:
        id = id[0] + (id[1]*2)
        if len(id) > 3:
            id = id[0] + (id[1])

    print('step 7 : ', id)
    return id

print(solution(new_id))
print(solution(new_id_2))
print(solution(new_id_3))
print(solution(new_id_4))
print(len(new_id_4))