from sklearn.base import BaseEstimator

class feature_engineering(BaseEstimator):
    
    def __init__(self):
        pass
    
    def fit(self, documents, y=None):
        return self
    
    def transform(self, x_dataset):
        top_screens = ['Loan2', 'location', 'Institutions', 'Credit3Container',
                       'VerifyPhone', 'BankVerification', 'VerifyDateOfBirth',
                       'ProfilePage', 'VerifyCountry', 'Cycle', 'idscreen',
                       'Credit3Dashboard', 'Loan3', 'CC1Category', 'Splash', 'Loan',
                       'CC1', 'RewardsContainer', 'Credit3', 'Credit1', 'EditProfile',
                       'Credit2', 'Finances', 'CC3', 'Saving9', 'Saving1', 'Alerts',
                       'Saving8', 'Saving10', 'Leaderboard', 'Saving4', 'VerifyMobile',
                       'VerifyHousing', 'RewardDetail', 'VerifyHousingAmount',
                       'ProfileMaritalStatus', 'ProfileChildren ', 'ProfileEducation',
                       'Saving7', 'ProfileEducationMajor', 'Rewards', 'AccountView',
                       'VerifyAnnualIncome', 'VerifyIncomeType', 'Saving2', 'Saving6',
                       'Saving2Amount', 'Saving5', 'ProfileJobTitle', 'Login',
                       'ProfileEmploymentLength', 'WebView', 'SecurityModal', 'Loan4',
                       'ResendToken', 'TransactionList', 'NetworkFailure', 'ListPicker']
        savings_screen = ["Saving1","Saving2","Saving2Amount","Saving4","Saving5","Saving6",
                          "Saving7","Saving8","Saving9","Saving10"]
        cc_screens = ["CC1","CC1Category","CC3"]
        loans_screens = ["Loan","Loan2","Loan3","Loan4"]
        
        try:
            
            x_dataset['hour'] = x_dataset.hour.str.slice(0,3).astype(int)
            x_dataset["first_open"] = [parser.parse(row_data) for row_data in x_dataset["first_open"]]
            x_dataset["enrolled_date"] = [parser.parse(row_data) if isinstance(row_data, str) else row_data for row_data in x_dataset["enrolled_date"]]
        
        except:
            pass
    
        x_dataset["screen_list"] = x_dataset.screen_list.astype(str)+','
        
        for sc in top_screens:
            x_dataset[sc] = x_dataset.screen_list.str.contains(sc).astype(int)
            x_dataset["screen_list"] = x_dataset.screen_list.replace(sc+","," ")
            
        x_dataset["other"] = x_dataset.screen_list.str.count(",")
        x_dataset["SavingCount"] = x_dataset[savings_screen].sum(axis=1)
        x_dataset = x_dataset.drop(columns= savings_screen)
        x_dataset["CCCount"] = x_dataset[cc_screens].sum(axis=1)
        x_dataset = x_dataset.drop(columns= cc_screens)
        x_dataset["LoansCount"] = x_dataset[loans_screens].sum(axis=1)
        x_dataset = x_dataset.drop(columns= loans_screens)
        
        return x_dataset