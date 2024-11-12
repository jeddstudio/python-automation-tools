import unittest
import os
import shutil  # 添加這行
from PIL import Image
from src.image_converter import ImageConverter

class TestImageConverter(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_images"
        os.makedirs(self.test_dir, exist_ok=True)
        self.converter = ImageConverter()

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_png_to_jpg_conversion(self):
        """Test converting PNG to JPG."""
        # Create a test PNG image
        test_image = Image.new('RGB', (100, 100), color='red')
        png_path = os.path.join(self.test_dir, "test.png")
        test_image.save(png_path)

        # Convert the image
        converted_files = self.converter.convert_directory(self.test_dir)
        
        # Verify conversion
        self.assertEqual(len(converted_files), 1)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "test.jpg")))

if __name__ == '__main__':
    unittest.main()