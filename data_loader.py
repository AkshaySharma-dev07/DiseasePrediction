import pandas as pd

def load_dataset():
    """Load the disease and symptom dataset."""
    file_path = "data/dataset.csv"
    df = pd.read_csv(file_path)

    return df

def clean_dataset(df):
    """Clean symptom names and remove empty values."""
    symptom_columns = [column for column in df.columns if column.startswith("Symptom_")]

    for column in symptom_columns:
        df[column] = (
            df[column]
            .fillna("")
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

    df["Disease"] = df["Disease"].str.strip()

    return df

def get_symptom_list(df):
    """Create a sorted list containing every unique symptom."""
    symptom_columns = [column for column in df.columns if column.startswith("Symptom_")]

    symptoms = set()

    for column in symptom_columns:
        for symptom in df[column]:
            if symptom:
                symptoms.add(symptom)

    return sorted(symptoms)

if __name__ == "__main__":
    data = load_dataset()
    data = clean_dataset(data)

    symptoms = get_symptom_list(data)

    print("Dataset loaded successfully!")
    print("Rows:", len(data))
    print("Diseases:", data["Disease"].nunique())
    print("Unique symptoms:", len(symptoms))
