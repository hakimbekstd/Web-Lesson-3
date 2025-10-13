def is_mountain(arr):
    n = len(arr)
    if n < 3:
        return False
    direction = 0 
    changed = False  
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            return False  
        if arr[i] > arr[i - 1]:
            if direction == -1:
                return False
            direction = 1
        else:
            if direction == 0:
                return False  
            direction = -1
            changed = True 
    return changed
print(is_mountain([1, 2, 3, 2, 1,2,3]))            # True
print(is_mountain([1, 2, 3]))                  # False (no down)
print(is_mountain([3, 2, 1]))                  # False (no up)
print(is_mountain([1, 2, 2, 1]))               # False (flat)
print(is_mountain([1, 2, 3, 2, 1, 2, 3]))      # False (goes up again)
print(is_mountain([0, 3, 2, 1])) 
print(is_mountain([2,2,2,3,1]))               # True
