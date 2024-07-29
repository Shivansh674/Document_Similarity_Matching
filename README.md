# Document Similarity Matching

## Overview

This project develops a system to identify and match similar invoices based on their content and structure. The system extracts text from PDF invoices, processes and compares them to find the most similar existing invoice.

## Setup

1. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

2. **Add Invoices**:
    - Place existing invoices in the `data/existing_invoices` directory.
    - Place the new invoices to compare in the `data` directory as `new_invoice.pdf` and `new_invoice1.pdf`.

## Running the Code

1. **Navigate to the Project Directory**:
    ```sh
    cd path/to/document_similarity_matching
    ```

2. **Activate the Virtual Environment** (if not already activated):
    - On Windows:
      ```sh
      .\venv\Scripts\activate
      ```

3. **Run the Main Script**:
    ```sh
    python scripts/main.py
    ```

## Explanation of Scripts

- `extract_text.py`: Contains the function to extract text from a PDF using Tika.
- `feature_extraction.py`: Extracts relevant features from the extracted text.
- `similarity_calculation.py`: Calculates cosine similarity between the feature vectors of two texts.
- `database_integration.py`: Adds invoices to an in-memory database and finds the most similar invoice.
- `main.py`: Orchestrates the process of extracting text, calculating similarity, and finding the most similar invoice from the database.

## Results

- The script will output the most similar invoice for each new invoice and its similarity score.
- The results will be saved in the `results` directory with filenames `similarity_scores_new_invoice.txt` and `similarity_scores_new_invoice1.txt`.

## Example Workflow

1. **Place Invoices**:
   - Ensure existing invoices are in `data/existing_invoices/`.
   - Ensure new invoices are named `new_invoice.pdf` and `new_invoice1.pdf` and placed in the `data/` directory.

2. **Run the Script**:
   ```sh
   python scripts/main.py
