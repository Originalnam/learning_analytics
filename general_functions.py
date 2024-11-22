import os
import sys
import pandas as pd
from pathlib import Path


# add the project directory to sys.path
project_root = os.path.dirname(os.path.abspath("__file__"))
sys.path.append(os.path.abspath(project_root))

def load_data(path= None):
    """
    Load all CSV files from the base data directory or a specified subfolder into a dictionary of DataFrames.
    
    Parameters:
    subfolder (str): The name of the subfolder within the base data directory. Default is an empty string for the base directory.
    
    Returns:
    dict: A dictionary where keys are table names (without the .csv extension) and values are the corresponding DataFrames.
    """    
    if path:
        # get table names
        files = os.listdir(path)
        csv_files = [file for file in files if file.endswith('.csv')]
        table_names = [file.split('.')[0] for file in csv_files]
        table_names

        # create dict of DataFrames for each table 
        dfs = {}

        for table_name in table_names:
            dfs[f'{table_name}'] = pd.read_csv(f'{path}{table_name}.csv')

        return dfs
    
    else:
        raise ValueError('Enter a path')
    
def write_data(dfs = None, path = None):
    if dfs and path:
        Path(path).mkdir(parents=True, exist_ok=True)

        dfs['courses'].to_csv(f'{path}courses.csv')
        dfs['assessments'].to_csv(f'{path}assessments.csv')
        dfs['vle'].to_csv(f'{path}vle.csv')
        dfs['studentInfo'].to_csv(f'{path}studentinfo.csv')
        dfs['studentRegistration'].to_csv(f'{path}studentregistration.csv')
        dfs['studentAssessment'].to_csv(f'{path}studentassessment.csv')
        dfs['studentVle'].to_csv(f'{path}studentvle.csv')
    else:
        raise ValueError("write_data() needs dfs and a path.")