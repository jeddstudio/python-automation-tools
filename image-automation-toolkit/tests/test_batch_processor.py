import unittest
import os
import shutil
from zipfile import ZipFile
from src.batch_processor import BatchProcessor

class TestBatchProcessor(unittest.TestCase):
    def setUp(self):
        self.test_dir = "test_files"
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        os.makedirs(self.test_dir)
        self.processor = BatchProcessor(self.test_dir)

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_process_directory_with_valid_zip(self):
        # 創建測試文件
        test_zip_name = "test.zip"
        test_zip_path = os.path.join(self.test_dir, test_zip_name)
        
        # 創建一個有內容的ZIP文件
        with ZipFile(test_zip_path, 'w') as zip_ref:
            # 創建一個真實的PNG文件
            png_data = bytes([137, 80, 78, 71, 13, 10, 26, 10]) + b'0' * 100  # PNG文件頭
            zip_ref.writestr("test.png", png_data)

        # 處理目錄
        processed_files = self.processor.process_directory()
        
        # 驗證結果
        self.assertEqual(len(processed_files), 1, "Should process exactly one file")
        expected_dir = os.path.join(self.test_dir, "test")
        self.assertTrue(os.path.exists(expected_dir), f"Directory {expected_dir} should exist")

if __name__ == '__main__':
    unittest.main()