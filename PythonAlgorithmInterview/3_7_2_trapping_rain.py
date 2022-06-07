# 빗물 트래핑
# 높이를 입력 받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라

# 투 포인터
def solution(height):
    max_height = max(height)
    width = len(height)
    total_space = max_height * width
    print(total_space)
    
    height_idx = height.index(max(height))
    print(height_idx)

def trap(height):
    if not height:
        return 0
    
    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    
    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1
    
    return volume
            
            
if __name__ == "__main__":
    rain = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(trap(rain))
    
    solution(rain)