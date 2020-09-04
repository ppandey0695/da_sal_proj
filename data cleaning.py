import pandas as pd
import numpy as np
df = pd.read_csv(r'C:/Users/praya/Documents/da_salary_proj/glassdoor_jobs.csv')


#SALARY PARSING

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_kd.apply (lambda x: x.lower().replace('per hour','').replace('employer provided salary',''))

df['min_sal'] = min_hr.apply(lambda x: int(x.split('-')[0]))
df['max_sal'] = min_hr.apply(lambda x: int(x.split('-')[1]))

df['avg_sal'] = (df.min_sal + df.max_sal)/2


#COMPANY

df['Company'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis = 1)
df


#PARSING LOCATION

df['City'] = df['Location'].apply(lambda x: x.split(',')[0])
df['State'] = df['Location'].apply(lambda x: x.split(',')[-1])


#AGE OF COMPANY

df['Age'] = df.Founded.apply(lambda x: x if x<1 else 2020 - x)
df


df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#df.python_yn.value_counts()

df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio' in x.lower() else 0)
#df._yn.value_counts()

df['Tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
#df.Tableau.value_counts()

df['SAS'] = df['Job Description'].apply(lambda x: 1 if 'sas' in x.lower() else 0)
#df.SAS.value_counts()

df['Apache'] = df['Job Description'].apply(lambda x: 1 if 'apache ' in x.lower() or 'spark' in x.lower() else 0)
#df.Apache.value_counts()

df['SQL'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
#df.SQL.value_counts()

df['Excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
#df.Excel.value_counts()

#COLUMNS TO DROP
df = df.drop(columns=['Salary Estimate','Company Name','Location', 'Headquarters','Competitors','Founded'], axis=1)


#EXPORTING TO CSV
df.to_csv('salary_data_cleaned.csv', index=False)

df = pd.read_csv(r'C:\Users\praya\Documents\da_salary_proj\salary_data_cleaned.csv')