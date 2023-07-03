import pandas as pd
import os
from dataclasses import dataclass


@dataclass
class DataTransformationConfig:

    transformed_file_path = os.path.join('artifacts','clean_data.csv')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self):
        try:
            df_raw = pd.read_csv(os.path.join('artifacts','raw.csv'))
            df_raw['year'] = df_raw['date'].apply(lambda x:x.split('-')[0]) 
            df_raw['month'] = df_raw['date'].apply(lambda x:x.split('-')[1]) 
            df_raw['day'] = df_raw['date'].apply(lambda x:x.split('-')[2]) 
            drop_columns = ['date']

            df_dropped= df_raw.drop(columns = drop_columns, axis=1)
            # df_grouped = df_dropped.groupby(['city_id','year','month','day','hour']).first()
            os.makedirs(os.path.dirname(self.data_transformation_config.transformed_file_path), exist_ok=True)

            df_dropped.to_csv(self.data_transformation_config.transformed_file_path, index=False)
            print(df_dropped.head())
            return self.data_transformation_config.transformed_file_path

            
        except Exception as e:
            print("an error occured",e)


