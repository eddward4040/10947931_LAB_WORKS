"""
Task 1: Image Loading and Grayscale Conversion
"""
import os
import cv2
from image_utils import ImageProcessor

def convert_to_grayscale(input_path: str, output_path: str) -> None:
    """
    Convert an image to grayscale and save it.
    
    Args:
        input_path (str): Path to the input image
        output_path (str): Path to save the grayscale image
    """
    try:
        # Initialize image processor
        processor = ImageProcessor()
        
        # Load the original image
        original_image = processor.load_image(input_path)
        
        # Convert to grayscale
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        
        # Display both images
        processor.display_images({
            'Original': original_image,
            'Grayscale': gray_image
        })
        
        # Save the grayscale image
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        processor.save_image(gray_image, output_path)
        print(f"Grayscale image saved successfully at: {output_path}")
    except Exception as e:
        print(f"Error in grayscale conversion: {str(e)}")
        raise