"""
Main script to run all image processing tasks.
This script provides a menu-driven interface to execute all three tasks.
"""
import os
import sys
from pathlib import Path
import cv2
import numpy as np
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Import task functions
from image_loading_and_grayscale_converter.task1 import process_image as task1_process
from color_space_converter_and_histogram.task2 import process_image as task2_process
from binary_thresholding_question.task3 import calculate_threshold_value

def check_image(image_path: str) -> bool:
    """
    Check if the image file exists and is valid.
    
        
    Returns:
        bool: True if image is valid, False otherwise
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return False
        
    try:
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error: Could not load image at {image_path}")
            return False
        return True
    except Exception as e:
        print(f"Error loading image: {str(e)}")
        return False

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Display the main menu."""
    print("\n=== Image Processing Tasks ===")
    print("1. Task 1: Image Loading and Grayscale Conversion")
    print("2. Task 2: Color Space Conversion and Histogram")
    print("3. Task 3: Binary Thresholding Example")
    print("4. Run All Tasks")
    print("5. Exit")
    print("==========================")

def run_task1():
    """Execute Task 1: Grayscale conversion."""
    print("\nRunning Task 1: Image Loading and Grayscale Conversion")
    try:
        input_path = os.path.join('images', 'photo.jpg')
        output_path = os.path.join('output', 'photo_gray.jpg')
        task1_process(input_path, output_path)
    except Exception as e:
        print(f"Error in Task 1: {str(e)}")
    input("\nPress Enter to continue...")

def run_task2():
    """Execute Task 2: Color space conversion and histogram."""
    print("\nRunning Task 2: Color Space Conversion and Histogram")
    try:
        input_path = os.path.join('images', 'photo.jpg')
        task2_process(input_path)
    except Exception as e:
        print(f"Error in Task 2: {str(e)}")
    input("\nPress Enter to continue...")

def run_task3():
    """Execute Task 3: Binary thresholding example."""
    print("\nTask 3: Binary Thresholding Example")
    pixel_value = 180
    threshold = 150
    result = calculate_threshold_value(pixel_value, threshold)
    
    print(f"Original pixel value: {pixel_value}")
    print(f"Threshold value: {threshold}")
    print(f"Result after thresholding: {result}")
    print("\nExplanation:")
    print(f"Since {pixel_value} > {threshold}, the output is {result}")
    input("\nPress Enter to continue...")

def run_all_tasks():
    """Execute all tasks in sequence."""
    print("\nRunning all tasks...")
    run_task1()
    run_task2()
    run_task3()

def main():
    """Main program loop."""
    while True:
        clear_screen()
        print_menu()
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            run_task1()
        elif choice == '2':
            run_task2()
        elif choice == '3':
            run_task3()
        elif choice == '4':
            run_all_tasks()
        elif choice == '5':
            print("\nThank you for using the Image Processing Tasks!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    # Ensure output directory exists
    os.makedirs('output', exist_ok=True)
    
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    
    # Check for input image
    image_path = os.path.join('images', 'photo.jpg')
    if not os.path.exists(image_path):
        print("\nNo image found! Please follow these steps:")
        print("1. Place an image file in the 'images' folder")
        print("2. Name it 'photo.jpg'")
        print("\nSupported formats: JPG, PNG, BMP")
        print(f"\nExpected path: {os.path.abspath(image_path)}")
        sys.exit(1)
        
    # Validate image
    if not check_image(image_path):
        print("\nPlease ensure the image file is not corrupted and is in a supported format.")
        sys.exit(1)
        
    main()
