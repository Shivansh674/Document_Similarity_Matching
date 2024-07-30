# Document Similarity Matching

## Overview

This project demonstrates a system for identifying and matching similar invoices based on their content and structure. The system extracts text from PDF invoices, computes features, and calculates similarity scores to find the most similar invoices from a database.

## Approach

### Document Representation Method

1. **Text Extraction**: 
   - The `text_extraction.py` script uses the Tika library to extract text content from PDF files.

2. **Feature Extraction**: 
   - The `feature_extraction.py` script extracts relevant features from the text, such as keywords, invoice numbers, dates, and amounts.

### Similarity Metric Used

- **Cosine Similarity**:
  - The `similarity_calculation.py` script calculates the cosine similarity between the feature vectors of two invoices using TF-IDF vectors.

## Instructions

### Setup

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Add Invoices**:
    - Place existing invoices in the `data/existing_invoices` directory.
    - Place the new invoice(s) to compare in the `data` directory (e.g., `new_invoice.pdf`).

### Running the Code

1. **Navigate to the Project Directory**:
    ```sh
    cd C:\Users\HP\document_similarity_matching
    ```

2. **Activate the Virtual Environment** (if not already activated):
    ```sh
    .\venv\Scripts\activate  # For Windows
    source venv/bin/activate  # For macOS/Linux
    ```

3. **Run the Main Script**:
    ```sh
    python scripts/main.py
    ```

### Explanation of the Scripts

- `text_extraction.py`: Extracts text from PDF invoices using Tika.
- `feature_extraction.py`: Extracts features from the extracted text.
- `similarity_calculation.py`: Calculates the cosine similarity between feature vectors.
- `database_integration.py`: Manages the invoice database and finds the most similar invoice.
- `main.py`: Coordinates the overall process of loading invoices, extracting text, computing features, and finding the most similar invoices.

## Results

The results are saved in the `results` directory. Each file contains the similarity scores for the corresponding new invoice compared against the main database.

### Example Output

- `similarity_scores_new_invoice.pdf.txt`:
    ```
    Most similar invoice: data/existing_invoices/invoice4.pdf
    Similarity score: 0.876
    ```

- `similarity_scores_new_invoice1.pdf.txt`:
    ```
    Most similar invoice: data/existing_invoices/invoice5.pdf
    Similarity score: 0.769
    ```

## Results Video

A screen recording with an explanation of the code, demonstration, and results of comparing the test cases against the main database is available at the following link:

[Results Video](https://drive.google.com/file/d/1h1MN4LiabN1csgpItqLIOMgtUR-P7L1e/view?usp=sharing) 

