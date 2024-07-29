from similarity_calculation import calculate_similarity

database = []

def add_invoice_to_database(invoice):
    database.append(invoice)

def find_most_similar_invoice(new_invoice):
    highest_similarity = 0
    most_similar_invoice = None
    for invoice in database:
        similarity = calculate_similarity(new_invoice['content'], invoice['content'])
        if similarity > highest_similarity:
            highest_similarity = similarity
            most_similar_invoice = invoice
    return most_similar_invoice, highest_similarity
