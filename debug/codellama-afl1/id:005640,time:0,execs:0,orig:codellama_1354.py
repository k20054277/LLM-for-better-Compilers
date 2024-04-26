import json

def get_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def test():
    data = get_data('example.json')
    assert len(data) == 2, "Incorrect number of elements in JSON file"
    assert data[0]['name'] == 'John', "Incorrect name for first element"
    assert data[1]['age'] == 30, "Incorrect age for second element"

if __name__ == '__main__':
    test()