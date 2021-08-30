import pandas as pd
import numpy as np
import os
from env import host, user, password


# connection url

# This function uses my info from the env file to create a connection url to access the Codeup db.
# It takes in a string name of a database as an argument.

def get_connection(db, user=user, host=host, password=password):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# acquiring data for the first time

def get_telco_churn():
    '''
    This function reads in the telco_churn data from the Codeup db
    and returns a pandas DataFrame with all columns and it was joined with other tables.
    '''
    sql_query = '''
    SELECT * 
    FROM customers
    JOIN contract_types USING (contract_type_id)
    JOIN internet_service_types USING (internet_service_type_id)
    JOIN payment_types USING (payment_type_id)
    '''
    return pd.read_sql(sql_query, get_connection('telco_churn'))


# main function to acquire project data

def get_telco_project():
    '''
    This function reads in telco_churn data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('telco_churn.csv'):
        
        # If csv file exists, read in data from csv file.
        df = pd.read_csv('telco_churn.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame.
        df = get_telco_churn()
        
        # Write DataFrame to a csv file.
        df.to_csv('telco_churn.csv')
        
    return df

