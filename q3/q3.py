import pandas as pd
import numpy as np

if __name__ == "__main__":
    data = {'unit price': [1000, 280, 900],
            'number': [25,120,30]}
    df = pd.DataFrame(data , index=['store1', 'store2', 'store3'], columns=['unit price', 'number'])
    print("DataFrame1")
    print(df,'\n')
    df['total price']=df['unit price']*df['number']
    print("DataFrame2")
    print(df,'\n')
    
    df2 = df.sort_values(by='total price', ascending=False)
    print("DataFrame3")
    print(df2.head(2))
    
    

    
