import os
from text_extraction import extract_text
from feature_extraction import extract_features
from database_integration import add_invoice_to_database, find_most_similar_invoice

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    existing_invoices = [
        os.path.join(base_dir, 'data/existing_invoices/invoice1.pdf'),
        os.path.join(base_dir, 'data/existing_invoices/invoice2.pdf'),
        os.path.join(base_dir, 'data/existing_invoices/invoice3.pdf'),
        os.path.join(base_dir, 'data/existing_invoices/invoice4.pdf'),
        os.path.join(base_dir, 'data/existing_invoices/invoice5.pdf')
    ]
    
    for invoice_path in existing_invoices:
        text = extract_text(invoice_path)
        features = extract_features(text)
        add_invoice_to_database({'path': invoice_path, 'content': text, 'features': features})
    
    new_invoices = [
        os.path.join(base_dir, 'data/new_invoice.pdf'),
        os.path.join(base_dir, 'data/new_invoice1.pdf')
    ]
    
    for new_invoice_path in new_invoices:
        new_text = extract_text(new_invoice_path)
        new_features = extract_features(new_text)
        most_similar_invoice, similarity_score = find_most_similar_invoice({'content': new_text, 'features': new_features})
        
        result_file_name = f'similarity_scores_{os.path.basename(new_invoice_path)}.txt'
        result_path = os.path.join(base_dir, 'results', result_file_name)
        with open(result_path, 'w') as f:
            f.write(f"Most similar invoice: {most_similar_invoice['path']}\n")
            f.write(f"Similarity score: {similarity_score}\n")
        
        print(f"Most similar invoice: {most_similar_invoice['path']}")
        print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()
