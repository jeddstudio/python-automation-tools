import unittest
import os
import shutil  # 添加這行
from PIL import Image
from src.pdf_generator import PDFGenerator

class TestPDFGenerator(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_images"
        os.makedirs(self.test_dir, exist_ok=True)
        self.generator = PDFGenerator()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_pdf_generation(self):
        """Test generating PDF from images."""
        # Create test images
        test_image = Image.new('RGB', (100, 100), color='red')
        test_image.save(os.path.join(self.test_dir, "test1.jpg"))
        test_image.save(os.path.join(self.test_dir, "test2.jpg"))

        # Generate PDF
        pdf_path = self.generator.create_pdf(self.test_dir, "output")
        
        # Verify PDF creation
        self.assertTrue(os.path.exists(pdf_path))
        self.assertTrue(pdf_path.endswith(".pdf"))

if __name__ == '__main__':
    unittest.main()