from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

print("Main is running")

def run_pipeline():
    print("Pipeline started")
    data = extract_data("data/netflix_titles.csv")
    print("Data extracted")
    transformed_data = transform_data(data)
    print("Data transformed")
    load_data(transformed_data)
    print("Pipeline loaded")

if __name__ == "__main__":
        print("Running the ETL pipeline")
        run_pipeline()
