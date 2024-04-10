import csv

def change_to_dict(file_name):
    """Change the csv format into list of dictionary format"""
    with open(file_name, 'r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
        return data
    
def dict_finder(file_name,name):
    """Find the matching name dictionary then output that dictionary"""
    data = change_to_dict(file_name)
    finder = lambda x : x["Name"] == name
    filtered = next(filter(finder, data))
    return filtered
            