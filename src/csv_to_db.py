import csv
from tinydb import TinyDB, Query
import os

def read_csv(file_path):
    # Read and parse the CSV file

    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    rel = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rel.append(row)
    return rel

def insert_into_db(data, db_path):
    
    # Check if data is empty
    if not data:
        raise ValueError("Data is empty")
    
    # Insert data into TinyDB
    db = TinyDB(db_path, indent=4)
    for record in data:
        db.insert(record)
    db.close()
    return data

def query_db(db_path, query_field, query_value):
    # Query the database
    db = TinyDB(db_path, indent=4)
    query = Query()
    results = db.search(query[query_field] == query_value)
    db.close()
    return results

if __name__ == "__main__":
    # Main execution logic
    pass