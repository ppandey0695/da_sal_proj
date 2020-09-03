
import glassdoor_scraper as gs
import pandas as pd

path = r"C:/Users/praya/Documents/da_salary_proj/chromedriver.exe"
df = gs.get_jobs('data analyst', 1000, False, path, 15)
df.to_csv('glassdoor_jobs.csv', index = False)


