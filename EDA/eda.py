# add project root to Python pathimport sys
import sys
from pathlib import Path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

import os
from general_functions import load_data, write_data

script_dir = os.path.dirname(os.path.abspath(__file__))

# load data
load_path = os.path.join(script_dir, '../data/')
dfs = load_data(load_path)

# data manipulation
# add presentation month to courses
dfs['courses'][['year', 'start_month']] = dfs['courses']['code_presentation'].str.extract(r'(\d{4})([A-Za-z])')
dfs['courses'].loc[dfs['courses']['start_month'] == 'J', 'start_month'] = 'October'
dfs['courses'].loc[dfs['courses']['start_month'] == 'B', 'start_month'] = 'February'

# change missing date of Exam assessments to last day of course
dfs['assessments']
dfs['assessments'].loc[
    (dfs['assessments']['date'].isna()) & 
    (dfs['assessments']['assessment_type'] == 'Exam'), 
    'date'
] = dfs['assessments'].merge(
    dfs['courses'][['code_module', 'code_presentation', 'module_presentation_length']], 
        on=['code_module', 'code_presentation']
        )['module_presentation_length']

# move changing columns from studentinfo to studenregistration 
dfs['studentRegistration'] = dfs['studentRegistration'].merge(
    dfs['studentInfo'][
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
dfs['studentInfo'] = dfs['studentInfo'].drop(
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
write_data(dfs, write_path)