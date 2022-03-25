# H-Index

def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    for idx in range(len(numbers)):
        if numbers[idx] <= len(numbers) - idx:
            answer = numbers[idx]
    return answer
