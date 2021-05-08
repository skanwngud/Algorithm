def solution(n, k, cmd):
    ori = ['O']*n
    de = []
    answer = 'O'*n
    
    for cd in cmd:
        if cd == 'C':
            if k == n-1 or 'O' not in ori[k+1:]:
                ori[k] = 'X'
                de.append(k)
                steps = 1
                while steps > 0:
                    k -= 1
                    if ori[k] == 'X':
                        continue
                    else:
                        steps -= 1
            
            else:
                try:
                    ori[k] = 'X'
                    de.append(k)
                    steps = 1
                    tmp_k = k
                    while steps > 0:
                        tmp_k += 1
                        if ori[tmp_k] == 'X':
                            continue
                        else:
                            steps -= 1
                    k = tmp_k
                    
                except:
                    ori[k] = 'X'
                    de.append(k)
                    steps = 1
                    while steps > 0:
                        k -= 1
                        if ori[k] == 'X':
                            continue
                        else:
                            steps -= 1
                            
        elif cd == 'Z':
            a = de.pop()
            ori[a] = 'O'
                
        else:
            to, steps = cd.split()
            steps = int(steps)
            if to == 'D':
                while steps > 0:
                    k += 1
                    if ori[k] == 'X':
                        continue
                    else:
                        steps -= 1
                        
            elif to == 'U':
                while steps > 0:
                    k -= 1
                    if ori[k] == 'X':
                        continue
                    else:
                        steps -= 1
    
    answer = ''.join(ori)
    return answer