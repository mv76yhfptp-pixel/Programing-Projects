import json

FILENAME = "Data Testing/Data.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)

            if not isinstance(data, list):
                return []
            return data

    except FileNotFoundError:
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=2)

if __name__ == "__main__":
    print("Data.py run successful")
else:
    print("Data.py Failed")