import unittest
from extract_pdf_text import extract_text_from_pdf

class TestExtractTextFromPdf(unittest.TestCase):
    def test_extract_text_from_pdf(self):
        # Arrange
        file_path = 'path/to/file.pdf'
        
        # Act
        text = extract_text_from_pdf(file_path)
        
        # Assert
        self.assertIsNotNone(text)
        self.assertGreater(len(text), 0)

if __name__ == '__main__':
    unittest.main()

