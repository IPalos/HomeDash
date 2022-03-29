import pandas as pd
import datetime
import random


# Objetivo 96 L por día por persona

base = datetime.date(2010,1,1)
date_list = [base + datetime.timedelta(days=x+1) for x in range(3650)]

water_consumption= [random.randrange(50,500) for i in range(3650)]
objective = [96 for i in range(3650)]



df = pd.DataFrame({'fecha':date_list, 'gasto':water_consumption, 'objetivo':objective})
