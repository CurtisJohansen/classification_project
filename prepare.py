
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

# prepare telco dataset 

def clean_telco_churn(df):

    #making dummies for columns I found appropriate to do so. I just went down the list. 

    df["is_female"] = df.gender == "Female"
    df['is_female'] = (df['is_female']).astype(int)

    df["partner"] = df.partner == "Yes"
    df['partner'] = (df['partner']).astype(int)

    df["dependents"] = df.dependents == "Yes"
    df['dependents'] = (df['dependents']).astype(int)

    df["phone_service"] = df.phone_service == "Yes"
    df['phone_service'] = (df['phone_service']).astype(int)

    df["streaming_tv"] = df.streaming_tv == "Yes"
    df['streaming_tv'] = (df['streaming_tv']).astype(int)

    df["streaming_movies"] = df.streaming_movies == "Yes"
    df['streaming_movies'] = (df['streaming_movies']).astype(int)

    df["paperless_billing"] = df.paperless_billing == "Yes"
    df['paperless_billing'] = (df['paperless_billing']).astype(int)

    df["churn"] = df.churn == "Yes"
    df['churn'] = (df['churn']).astype(int)

    df["multiple_lines"] = df.multiple_lines == "Yes"
    df['multiple_lines'] = (df['multiple_lines']).astype(int)

    df["online_security"] = df.online_security == "Yes"
    df['online_security'] = (df['online_security']).astype(int)

    df["online_backup"] = df.online_backup == "Yes"
    df['online_backup'] = (df['online_backup']).astype(int)

    df["device_protection"] = df.device_protection == "Yes"
    df['device_protection'] = (df['device_protection']).astype(int)

    df["tech_support"] = df.tech_support == "Yes"
    df['tech_support'] = (df['tech_support']).astype(int)

    # adding a column is_auto_pay to identify if customer pays automatically or manually.
    # is_auto_pay, 1 is True, 0 is False

    df['is_auto_pay'] = df.payment_type.replace(["Mailed check", "Electronic check", "Credit card (automatic)", "Bank transfer (automatic)"], [0,0,1,1])
    
    # 11 blank values in the total_charges column that represent only new customers with less than 1 month of tenure 
    # replaced the blanks with a 0 (float)

    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    

    # dropping columns not needed 

    df = df.drop(columns =['payment_type_id', 'contract_type_id', 'internet_service_type_id'])
    df = df.drop(columns=['gender'])

    # making a dummy df and combining back into original df

    dummy_df = pd.get_dummies(df[['internet_service_type', 'contract_type','payment_type']], drop_first=False)
    dummy_df = dummy_df.rename(columns={'internet_service_type_DSL': 'dsl',
                                   'internet_service_type_Fiber optic': 'fiber_optic',
                                   'internet_service_type_None': 'no_internet',
                                   'contract_type_Month-to-month': 'monthly',
                                   'contract_type_One year': 'one_year',
                                   'contract_type_Two year': 'two_year',
                                   'payment_type_Bank transfer (automatic)': 'bank_transfer',
                                   'payment_type_Credit card (automatic)': 'credit_card',
                                   'payment_type_Electronic check': 'electronic_check',
                                   'payment_type_Mailed check': 'mailed_check'})
    df = pd.concat([df, dummy_df], axis =1)

    return df 
    
    
    
    
# splitting data - returns train, validate, and test dfs
    
def telco_churn_split(df):
    
    train_validate, test = train_test_split(df, test_size=.2, 
                                            random_state=123, 
                                            stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    
    return train, validate, test


# prep function cleans and splits data and returns the train, validate and test splits

def prep_telco_churn(df):
    df = clean_telco_churn(df)
    train, validate, test = telco_churn_split(df)
    return train, validate, test
    
#def prep_telco_churn(get_telco_project):
 #   df = clean_telco_churn(df)
 #   train, validate, test = telco_churn_split(df)
  #  return train, validate, test
