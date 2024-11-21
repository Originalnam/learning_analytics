import os
import pandas as pd
from pathlib import Path

# load data
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, '../data/')
files = os.listdir(path)
csv_files = [file for file in files if file.endswith('.csv')]
table_names = [file.split('.')[0] for file in csv_files]

dfs = {}

for table_name in table_names:
    dfs[f'{table_name}'] = pd.read_csv(f'{path}{table_name}.csv')

# data manipulation
df_courses = dfs['courses']
df_assessments = dfs['assessments']
df_vle = dfs['vle']
df_studentinfo = dfs['studentInfo']
df_studentregistration = dfs['studentRegistration']
df_studentassessment = dfs['studentAssessment']
df_studentvle = dfs['studentVle']

# add presentation month to courses
df_courses = dfs['courses']
df_courses[['year', 'start_month']] = df_courses['code_presentation'].str.extract(r'(\d{4})([A-Za-z])')
df_courses.loc[df_courses['start_month'] == 'J', 'start_month'] = 'October'
df_courses.loc[df_courses['start_month'] == 'B', 'start_month'] = 'February'

# change missing date of Exam assessments to last day of course
df_assessments = dfs['assessments']
df_assessments.loc[
    (df_assessments['date'].isna()) & 
    (df_assessments['assessment_type'] == 'Exam'), 
    'date'
] = df_assessments.merge(
    df_courses[['code_module', 'code_presentation', 'module_presentation_length']], 
        on=['code_module', 'code_presentation']
        )['module_presentation_length']

# move changing columns from studentinfo to studenregistration 
df_studentregistration = df_studentregistration.merge(
    df_studentinfo[
        ['id_student',
         'age_band', 
         'imd_band', 
         'studied_credits', 
         'num_of_prev_attempts', 
         'final_result', 
         'code_module', 
         'code_presentation']
         ], 
         on=['id_student', 
             'code_module', 
             'code_presentation'
             ]
             )
df_studentinfo = df_studentinfo.drop(
    columns=[
        'code_module',
        'code_presentation',
        'imd_band', 
        'age_band', 
        'num_of_prev_attempts', 
        'studied_credits', 
        'final_result'
        ]
        ).drop_duplicates()

# write data
write_path = os.path.join(script_dir, '../data/EDA/')
Path(write_path).mkdir(parents=True, exist_ok=True)

df_courses.to_csv(f'{write_path}courses.csv')
df_assessments.to_csv(f'{write_path}assessments.csv')
df_vle.to_csv(f'{write_path}vle.csv')
df_studentinfo.to_csv(f'{write_path}studentinfo.csv')
df_studentregistration.to_csv(f'{write_path}studentregistration.csv')
df_studentassessment.to_csv(f'{write_path}studentassessment.csv')
df_studentvle.to_csv(f'{write_path}studentvle.csv')