[PYTHON]
def save_object(obj, filename):
    with open(filename, "wb") as f:
        pickle.dump(obj, f)

def load_object(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)
[/PYTHON]