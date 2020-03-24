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

#API definition
app = Flask(__name__)
CORS(app)
#load model
model_AI = pickle.load(open('model_rfc.pkl','rb'))

@app.route('/ai', methods=['POST'])
def ai():
	try:
		
		json_ = request.json

		dayofweek = float(json_["dayofweek"])
		hour = float(json_["hour"])
		age = float(json_["age"])
		numscreens = float(json_["numscreens"])
		minigame = float(json_["minigame"])
		used_premium_feature= float(json_["used_premium_feature"])
		liked = float(json_["liked"])
		location = float(json_["location"])
		Institutions = float(json_["Institutions"])
		Credit3Container = float(json_["Credit3Container"])
		VerifyPhone = float(json_["VerifyPhone"])
		BankVerification = float(json_["BankVerification"])
		VerifyDateOfBirth = float(json_["VerifyDateOfBirth"])
		ProfilePage = float(json_["ProfilePage"])
		VerifyCountry = float(json_["VerifyCountry"])
		Cycle = float(json_["Cycle"])
		idscreen = float(json_["idscreen"])
		Credit3Dashboard = float(json_["Credit3Dashboard"])
		Splash = float(json_["Splash"])
		RewardsContainer = float(json_["RewardsContainer"])
		Credit3 = float(json_["Credit3"])
		Credit1 = float(json_["Credit1"])
		EditProfile =  float(json_["EditProfile"])
		Credit2 = float(json_["Credit2"])
		Finances =  float(json_["Finances"])
		Alerts =  float(json_["Alerts"])
		Leaderboard =  float(json_["Leaderboard"])
		VerifyMobile =  float(json_["VerifyMobile"])
		VerifyHousing = float(json_["VerifyHousing"])
		ProfileMaritalStatus = float(json_["ProfileMaritalStatus"])
		ProfileEducation = float(json_["ProfileEducation"])
		AccountView =  float(json_["AccountView"])
		VerifyIncomeType = float(json_["VerifyIncomeType"])
		Login =  float(json_["Login"])
		WebView = float(json_["WebView"])
		ResendToken = float(json_["ResendToken"])
		TransactionList = float(json_["TransactionList"])
		ListPicker = float(json_["ListPicker"])
		other = float(json_["other"])
		SavingCount =  float(json_["SavingCount"])
		LoansCount =  float(json_["LoansCount"])
		
		data_temp = [dayofweek, hour, age, numscreens, minigame, used_premium_feature, liked, location, Institutions, Credit3Container, VerifyPhone, BankVerification, VerifyDateOfBirth, ProfilePage, VerifyCountry, Cycle, idscreen, Credit3Dashboard, Splash, RewardsContainer, Credit3, Credit1, EditProfile, Credit2, Finances, Alerts, Leaderboard, VerifyMobile, VerifyHousing, ProfileMaritalStatus, ProfileEducation, AccountView, VerifyIncomeType, Login, WebView, ResendToken, TransactionList, ListPicker, other, SavingCount, LoansCount]
		data_columns = ["dayofweek", "hour", "age", "numscreens", "minigame", "used_premium_feature", "liked", "location", "Institutions", "Credit3Container", "VerifyPhone", "BankVerification", "VerifyDateOfBirth", "ProfilePage", "VerifyCountry", "Cycle", "idscreen", "Credit3Dashboard", "Splash", "RewardsContainer", "Credit3","Credit1", "EditProfile", "Credit2", "Finances", "Alerts", "Leaderboard", "VerifyMobile", "VerifyHousing", "ProfileMaritalStatus","ProfileEducation", "AccountView", "VerifyIncomeType", "Login", "WebView", "ResendToken", "TransactionList", "ListPicker", "other", "SavingCount", "LoansCount"]
		data_df = pd.DataFrame([data_temp], columns=data_columns, index=[0])

		prob_default = model_AI.predict_proba(data_df)[0,0]
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
