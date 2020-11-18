import subprocess
import pandas as pd
from datetime import datetime, timedelta, date

cur_date=date.today()
print(type(cur_date))
df=pd.read_excel("postingxlsx.xlsx")
print(df)

for i,row in df.iterrows():
     if cur_date==row['Date']:
          post_time=str(row['Time'])
          print(post_time)
          j=str(i)
          command = "SCHTASKS /CREATE /SC ONCE /TN test"+j+" /TR d:\pycharm\sco_poster.py /ST "+post_time+""
          subprocess.run(command, shell=True)



