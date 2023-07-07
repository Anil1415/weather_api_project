from flask import Flask, request, jsonify
import pandas as pd
import os
import json

# initialising a flask app

application = Flask(__name__)

app = application

@app.route('/', methods = ['GET'])
def home_page():
    return 'Welcome to weather Data'


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

@app.route('/weather/range', methods = ['GET'])
def output_range():
    df=pd.read_csv(os.path.join('artifacts','clean_data.csv'))
    df_grouped = df.groupby(['city_id','year','month','day','hour']).first()
    # starting values
    city_id = request.args.get(key='start_city_id', type=int)
    year = request.args.get(key='start_year',type=int)
    month = request.args.get(key='start_month',type=int)
    day = request.args.get(key='start_day',type=int)
    hour = request.args.get(key='start_hour',type=int)
    start_index_value = (city_id,year,month,day,hour)
    print(start_index_value)

    # ending values
    city_id = request.args.get(key='end_city_id', type=int)
    year = request.args.get(key='end_year',type=int)
    month = request.args.get(key='end_month',type=int)
    day = request.args.get(key='end_day',type=int)
    hour = request.args.get(key='end_hour',type=int)
    end_index_value = (city_id,year,month,day,hour)
    print(end_index_value)
   
    result = df_grouped.loc[start_index_value:end_index_value, :]
    print(result.head())
    str_obj = result.to_json()
    print(str_obj)
    js_dict = json.loads(str_obj)

    
    return jsonify(js_dict)


    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5000)


        
       


        