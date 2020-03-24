import traceback
import pandas as pd
import numpy as np
import pickle
import datetime
import dill
from dateutil.relativedelta import relativedelta
from flask import Flask, request, jsonify, json, make_response
from flask_cors import CORS
from mysql import connector
from description import get_ai_grade
#from sklearn.base import BaseEstimator
from fitur import feature_engineering

#API definition
app = Flask(__name__)
CORS(app)

#load model
model_AI = pickle.load(open('full_pipeline_rfc.pkl','rb'))


@app.route('/ai', methods=['POST'])
def ai():
	try:
		

		json_ = request.json

		user = float(json_["user"]) 
		first_open = json_['first_open']
		dayofweek = float(json_['dayofweek']) 
		hour = json_['hour']
		age = float(json_['age'])
		screen_list = json_['screen_list']
		numscreens = float(json_['numscreens'])
		minigame = float(json_['minigame']) 
		used_premium_feature = float(json_['used_premium_feature'])
		enrolled = float(json_['enrolled'])
		enrolled_date = json_['enrolled_date']
		liked = float(json_['liked'])
		
		data_temp = [user, first_open, dayofweek, hour, age, screen_list, numscreens, minigame, used_premium_feature, enrolled, enrolled_date, liked]
		data_columns = ["user", "first_open", "dayofweek", "hour", "age", "screen_list","numscreens", "minigame", "used_premium_feature", "enrolled","enrolled_date", "liked"]
		data_df = pd.DataFrame([data_temp], columns=data_columns, index=[0])

		prob_default = model_AI.predict_proba(data_df)[:,1]
		grade = get_ai_grade(prob_default*100)

		out_dict = dict()
		out_dict['prob_default'] = round((float(prob_default))*100, 3)
		out_dict['Grade'] = grade

		return jsonify(out_dict)

	except:

		return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':

	port = 2020

	app.run(host='localhost', port=port, debug=True)
