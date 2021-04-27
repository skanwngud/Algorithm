# 절댓값 구하기
import math

def abs_sign(a):
    if a>=0:
        return a
    else:
        return -a # 음수인 경우 - 를 곱해 -(-a) = +a 가 된다

def square(a):
    b = a*a
    return math.sqrt(b)

print(abs_sign(1)) # 1
print(abs_sign(-1)) # 1
print(abs_sign(-3)) # 3
print(abs_sign(5)) # 5
print(abs_sign(-10)) # 10

print(square(1)) # 1.0
print(square(-1)) # 1.0
print(square(-3)) # 3.0
print(square(5)) # 5.0
print(square(-10)) # 10.0 - 제곱근은 float type 으로 출력한다. 값 앞에 int 를 붙이면 int type 으로 변함