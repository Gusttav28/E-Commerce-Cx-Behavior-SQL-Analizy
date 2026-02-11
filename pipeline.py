import pandas as pd
import mysql.connector
from sqlalchemy import create_engine


def extracting_data(file_path):
    return pd.read_csv(file_path)

def loading_data(df, db_name):
    connection_string = f"mysql+mysqlconnector://root:30696222@localhost/{db_name}"
    engine = create_engine(connection_string)
    df.to_sql(db_name, con=engine, if_exists='append', index=False)



if __name__ == "__main__":
    raw_df = extracting_data("ecommerce_customer_behavior_5000.csv")
    loading_data = loading_data(raw_df, "e-commerce-behavior")
    print("Data succesfully merge into mysql")