from numpy import fabs
import pandas as pd
import os, sys,openpyxl

# read file as source
# Extraction Phase 
source_file_txt = pd.read_csv(os.path.join(sys.path[0],'sample_source.txt'))

# trasformation phase

# remove null from dataset
transform_data = source_file_txt.dropna()
# filter salary more than 25 
df_salary_more_than_25 = transform_data[transform_data['salary']>25]


# load phase
target_sample = df_salary_more_than_25.to_excel(os.path.join(sys.path[0],'Target_sample.xlsx'),index=False)


def test_salary_more_than_25(salary_emp,x):
    for i in salary_emp:
        if i<=x:
            return False
    else:
        return True

