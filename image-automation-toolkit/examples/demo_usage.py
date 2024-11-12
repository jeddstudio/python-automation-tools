from src.batch_processor import BatchProcessor
from src.image_converter import ImageConverter
from src.pdf_generator import PDFGenerator

def main():
    # Initialize components
    processor = BatchProcessor()
    converter = ImageConverter()
    pdf_gen = PDFGenerator()
    
    # Process all zip files
    processed_dirs = processor.process_directory()
    
    # Convert images and generate PDFs for each processed directory
    for dir_name in processed_dirs:
        # Convert PNGs to JPGs
        converter.convert_directory(dir_name)
        
        # Generate PDF
        pdf_gen.create_pdf(dir_name, dir_name)

if __name__ == "__main__":
    main()