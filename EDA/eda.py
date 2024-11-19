import os
import pandas as pd

# load data
path = '../data/'
files = os.listdir(path)
csv_files = [file for file in files if file.endswith('.csv')]
table_names = [file.split('.')[0] for file in csv_files]

dfs = {}

for table_name in table_names:
    dfs[f'{table_name}'] = pd.read_csv(f'{path}{table_name}.csv')

# data manipulation
## add presentation month to courses
df_courses = dfs['courses']
df_courses[['year', 'start_month']] = df_courses['code_presentation'].str.extract(r'(\d{4})([A-Za-z])')
df_courses.loc[df_courses['start_month'] == 'J', 'start_month'] = 'October'
df_courses.loc[df_courses['start_month'] == 'B', 'steart_month'] = 'February'

## change missing date of Exam assessments to last day of course
df_assessments = dfs['assessments']
df_assessments.loc[
    (df_assessments['date'].isna()) & 
    (df_assessments['assessment_type'] == 'Exam'), 
    'date'
] = df_assessments.merge(
    df_courses[['code_module', 'code_presentation', 'module_presentation_length']], 
        on=['code_module', 'code_presentation']
        )['module_presentation_length']

## vle