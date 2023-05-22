import numpy as np
import pandas as pd
import csv


if __name__ == "__main__":

    df = pd.read_csv('gender2.csv',encoding='cp949')

    locate = df['행정구역'].values.tolist()
    male = df['2022년_남_총인구수'].values.tolist()
    female = df['2022년_여_총인구수'].values.tolist()
    total = df['2022년_계_총인구수'].values.tolist()

    data = {'Total': total,
            'Male': male,
            'Female': female}
    
    newdf = pd.DataFrame(data,index=locate)
    print(newdf)
