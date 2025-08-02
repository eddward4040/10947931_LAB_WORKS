"""
Task 2: Color Space Conversion and Histogram
"""
import os
import cv2
from image_utils import ImageProcessor

def process_color_spaces(input_path: str) -> None:
    """
    Convert an image to different color spaces and plot histogram.
    
    Args:
        input_path (str): Path to the input image
    """
    # Initialize image processor
    processor = ImageProcessor()
    
    # Define paths
    output_path_gray = os.path.join('output', 'photo_grayscale.jpg')
    output_path_hsv = os.path.join('output', 'photo_hsv.jpg')
    output_path_lab = os.path.join('output', 'photo_lab.jpg')
    output_path_histogram = os.path.join('output', 'histogram.png')
    
    try:
        # Load the original image
        original_image = processor.load_image(input_path)
        
        # Convert to different color spaces
        gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)
        lab_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2LAB)
        
        # Display all images
        processor.display_images({
            'Original': original_image,
            'Grayscale': gray_image,
            'HSV': hsv_image,
            'LAB': lab_image
        })
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path_gray), exist_ok=True)
        
        # Save converted images
        processor.save_image(gray_image, output_path_gray)
        processor.save_image(hsv_image, output_path_hsv)
        processor.save_image(lab_image, output_path_lab)
        
        # Plot and save histogram
        processor.plot_histogram(gray_image, output_path_histogram)
        
        print("All images and histogram saved successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main()