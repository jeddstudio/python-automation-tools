import os
import logging
from zipfile import ZipFile
from typing import List, Optional
from datetime import datetime

class BatchProcessor:
    def __init__(self, working_dir: Optional[str] = None):
        self.working_dir = working_dir or os.getcwd()
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging with timestamp and level."""
        logging.basicConfig(
            filename=f'batch_process_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def process_directory(self) -> List[str]:
        """
        Process all zip files in the working directory.
        Returns list of processed files.
        """
        processed_files = []
        
        for zip_file in os.listdir(self.working_dir):
            if not zip_file.endswith(('.zip', '.rar')):
                continue
                
            try:
                clean_name = os.path.splitext(zip_file)[0]
                output_dir = os.path.join(self.working_dir, clean_name)
                
                self.logger.info(f"Processing {zip_file}")
                
                # Create output directory
                os.makedirs(output_dir, exist_ok=True)
                
                # Extract archive
                zip_path = os.path.join(self.working_dir, zip_file)
                if zip_file.endswith('.zip'):
                    with ZipFile(zip_path, 'r') as zip_ref:
                        zip_ref.extractall(output_dir)
                    processed_files.append(clean_name)
                    self.logger.info(f"Successfully processed {zip_file}")
                
            except Exception as e:
                self.logger.error(f"Error processing {zip_file}: {str(e)}")
                continue
                
        return processed_files