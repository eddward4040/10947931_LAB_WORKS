"""
Task 3: Binary Thresholding Question and Implementation
"""

def calculate_threshold_value(pixel_value: int, threshold: int) -> int:
    """
    Calculate the new pixel value after binary thresholding.
    
    Args:
        pixel_value (int): Original pixel value
        threshold (int): Threshold value
        
    Returns:
        int: New pixel value after thresholding (0 or 255)
    """
    return 255 if pixel_value > threshold else 0

def main():
    # Given values
    pixel_value = 180
    threshold = 150
    
    # Calculate new pixel value
    new_pixel_value = calculate_threshold_value(pixel_value, threshold)
    
    # Print the result
    print(f"Original pixel value: {pixel_value}")
    print(f"Threshold value: {threshold}")
    print(f"New pixel value after thresholding: {new_pixel_value}")
    
    # Explanation
    print("\nExplanation:")
    print("Since the original pixel value (180) is greater than")
    print("the threshold value (150), the new pixel value is set to 255.")
    print("This is how binary thresholding works - pixels above the")
    print("threshold become white (255) and pixels below become black (0).")

if __name__ == "__main__":
    main()