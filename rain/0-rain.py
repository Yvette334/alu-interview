#!/usr/bin/python3
def rain(walls):
    """
    Calculate how many square units of water will be retained after it rains.
    
    Args:
        walls: List of non-negative integers representing wall heights
        
    Returns:
        Integer indicating total amount of rainwater retained
    """
    if not walls or len(walls) < 3:
        return 0
    
    n = len(walls)
    total_water = 0
    
    # For each position, find the maximum height to the left and right
    for i in range(1, n - 1):  # Skip first and last positions
        # Find maximum height to the left
        left_max = max(walls[:i])
        
        # Find maximum height to the right
        right_max = max(walls[i + 1:])
        
        # Water level at position i is min of left_max and right_max
        water_level = min(left_max, right_max)
        
        # Water trapped = water_level - current_height (if positive)
        water_trapped = max(0, water_level - walls[i])
        total_water += water_trapped
    
    return total_water

# Test with the provided examples
if __name__ == "__main__":
    # Test case 1: [0, 1, 0, 2, 0, 3, 0, 4]
    walls1 = [0, 1, 0, 2, 0, 3, 0, 4]
    result1 = rain(walls1)
    print(f"Walls: {walls1}")
    print(f"Water trapped: {result1}")
    print()
    
    # Test case 2: [2, 0, 0, 4, 0, 0, 1, 0]
    walls2 = [2, 0, 0, 4, 0, 0, 1, 0]
    result2 = rain(walls2)
    print(f"Walls: {walls2}")
    print(f"Water trapped: {result2}")
    print()
    
    # Let's trace through the first example step by step
    print("Detailed trace for [0, 1, 0, 2, 0, 3, 0, 4]:")
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    total = 0
    
    for i in range(1, len(walls) - 1):
        left_max = max(walls[:i])
        right_max = max(walls[i + 1:])
        water_level = min(left_max, right_max)
        water_trapped = max(0, water_level - walls[i])
        total += water_trapped
        
        print(f"Position {i}: height={walls[i]}, left_max={left_max}, right_max={right_max}, water_level={water_level}, trapped={water_trapped}")
    
    print(f"Total water trapped: {total}")
