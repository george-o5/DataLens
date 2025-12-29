import csv

def load_docking_data(file_path):
    data = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def get_top_molecule(data):
    # lower (more negative) docking score = better
    best = min(data, key=lambda x: float(x["docking_score"]))
    return best

def main():
    data = load_docking_data("../data/docking_results.csv")
    top = get_top_molecule(data)

    print(
        f"Top molecule based on docking score: "
        f"{top['molecule']} ({top['docking_score']})"
    )

if __name__ == "__main__":
    main()
