from flask import Flask, request, jsonify
import pandas as pd
import os


# initialising a flask app

application = Flask(__name__)

app = application

@app.route('/', methods = ['GET'])
def home_page():
    return 'Anil'

@app.route('/weather', methods = ['GET'])
def get_output():

        
    df=pd.read_csv(os.path.join('artifacts','clean_data.csv'))
    df_grouped = df.groupby(['city_id','year','month','day','hour']).first()
    city_id = request.args.get(key='city_id', type=int)
    year = request.args.get(key='year',type=int)
    month = request.args.get(key='month',type=int)
    day = request.args.get(key='day',type=int)
    hour = request.args.get(key='hour',type=int)
    index_value = (city_id,year,month,day,hour)
    print(index_value)
    print(df_grouped.loc[index_value, :])
    print(df_grouped.loc[index_value, :].to_dict())
    return df_grouped.loc[index_value, :].to_dict()
        



if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000)

"""

        city_id = request.args.get(key='date', type=int)
        year = request.args.get(key='year',type=int)
        month = request.args.get(key='month',type=int)
        day = request.args.get(key='day',type=int)
        hour = request.args.get(key='hour',type=int)
"""







