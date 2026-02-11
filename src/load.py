from sqlalchemy import create_engine

def load_data(data):

    engine = create_engine("postgresql://postgres:StrongPassword123@localhost:5432/postgres")
    data.to_sql("netflix_data", engine, if_exists="replace", index=False)

    print("Data loaded successfully into the database")