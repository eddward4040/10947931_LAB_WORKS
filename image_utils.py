"""
Utility functions for image processing tasks.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple

class ImageProcessor:
    @staticmethod
    def load_image(image_path: str) -> np.ndarray:
        """
        Load an image from the specified path.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            np.ndarray: Loaded image
        """
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Could not load image from {image_path}")
        return image

    @staticmethod
    def save_image(image: np.ndarray, output_path: str) -> None:
        """
        Save an image to the specified path.
        
        Args:
            image (np.ndarray): Image to save
            output_path (str): Path where to save the image
        """
        cv2.imwrite(output_path, image)

    @staticmethod
    def display_images(images: dict) -> None:
        """
        Display multiple images using matplotlib.
        
        Args:
            images (dict): Dictionary of images with their titles
        """
        n = len(images)
        plt.figure(figsize=(15, 5))
        
        for idx, (title, img) in enumerate(images.items(), 1):
            plt.subplot(1, n, idx)
            
            # Convert BGR to RGB for display
            if len(img.shape) == 3:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                
            plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
            plt.title(title)
            plt.axis('off')
            
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_histogram(gray_image: np.ndarray, save_path: str = None) -> None:
        """
        Plot and optionally save histogram of a grayscale image.
        
        Args:
            gray_image (np.ndarray): Grayscale image
            save_path (str, optional): Path to save the histogram plot
        """
        plt.figure(figsize=(10, 5))
        plt.hist(gray_image.ravel(), 256, [0, 256])
        plt.title('Grayscale Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')
        
        if save_path:
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(save_path)
        
        plt.show()