def solution(numbers):
    answer = 0
    numbers = sorted(numbers)
    for idx in range(len(numbers)):
        print(len(numbers[idx:]))
        if numbers[idx] <= len(numbers[idx:]):
            answer = numbers[idx]
    return answer

def solution2(numbers):
    answer = 0
    numbers = sorted(numbers)
    for idx in range(len(numbers)):
        print(len(numbers) - idx)
        if numbers[idx] <= len(numbers) - idx:
            answer = numbers[idx]
    return answer

def solution3(numbers):
    answer = 0
    numbers.sort(reverse=True)
    print(numbers)

if __name__ == "__main__":
    numbers = [0, 1, 4, 3, 5, 7, 9]
    print('1', solution(numbers))
    print('2', solution2(numbers))
    print(solution3(numbers))