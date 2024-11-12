from PIL import Image
import os
import logging
from typing import List, Tuple
from pathlib import Path

class ImageConverter:
    """
    Handles image format conversion and optimization.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def convert_directory(self, directory: str) -> List[str]:
        """
        Convert all PNG images in directory to JPG format.
        Returns list of converted files.
        """
        converted_files = []
        directory_path = Path(directory)
        
        for png_file in directory_path.glob("*.png"):
            try:
                jpg_path = self.convert_to_jpg(png_file)
                converted_files.append(jpg_path)
                os.remove(png_file)  # Remove original PNG after successful conversion
                self.logger.info(f"Converted and removed: {png_file}")
            except Exception as e:
                self.logger.error(f"Failed to convert {png_file}: {str(e)}")
                continue
                
        return converted_files
    
    def convert_to_jpg(self, png_path: Path) -> str:
        """Convert single PNG file to JPG format."""
        jpg_path = png_path.with_suffix('.jpg')
        
        with Image.open(png_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_path, quality=95, optimize=True)
            
        return str(jpg_path)