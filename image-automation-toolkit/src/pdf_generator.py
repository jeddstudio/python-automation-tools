import img2pdf
import os
import logging
from typing import List
from pathlib import Path

class PDFGenerator:
    """
    Handles PDF generation from image files.
    """
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def create_pdf(self, image_dir: str, output_name: str) -> str:
        """
        Create PDF from all images in directory.
        Returns path to generated PDF.
        """
        try:
            image_dir_path = Path(image_dir)
            pdf_path = image_dir_path / f"{output_name}.pdf"
            
            # Collect and sort image paths
            image_paths = self._collect_images(image_dir_path)
            
            if not image_paths:
                raise ValueError("No valid images found in directory")
            
            # Generate PDF
            with open(pdf_path, "wb") as pdf_file:
                pdf_file.write(img2pdf.convert(image_paths))
                
            self.logger.info(f"Created PDF: {pdf_path}")
            return str(pdf_path)
            
        except Exception as e:
            self.logger.error(f"Failed to create PDF: {str(e)}")
            raise
            
    def _collect_images(self, directory: Path) -> List[str]:
        """Collect all image files from directory and sort them."""
        image_paths = []
        
        for img_path in directory.glob("*.[jp][pn][g]"):  # Match jpg, jpeg, png
            if img_path.is_file():
                image_paths.append(str(img_path))
                
        return sorted(image_paths)