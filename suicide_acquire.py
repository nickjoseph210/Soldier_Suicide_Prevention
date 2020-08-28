import pandas as pd
import numpy as np

import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute
from sklearn.model_selection import train_test_split

# Google Sheet imports are tagged with the following keyword arguments: sep=None, thousands=",", and engine="python"
# This was in an effort to import the spreadsheet data without having to go back in and remove / replace commas and spaces
# with either regex or python commands.

# -------------- Age-Adjusted_DataFrame ----------------

def age_adjusted():
    """
    Function to import the first of the analyzed DataFrames, the 'age_adjusted' DataFrame
    """
    
    # original link: https://docs.google.com/spreadsheets/d/18QZWC80YlnF8eMYUugbdtrnzif9fuANos8XZJ_2j27w/edit?usp=sharing
    sheet1_id = "18QZWC80YlnF8eMYUugbdtrnzif9fuANos8XZJ_2j27w"

    age_adjusted_df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet1_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns
    age_adjusted_df = age_adjusted_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "total_vet_suicides",
                "Unnamed: 2": "est_total_vet_pop",
                "Unnamed: 3": "veteran_crude_rate_per_100K",
                "Unnamed: 4": "age_adjusted_rate_per_100K",
                "Unnamed: 5": "male_suicides",
                "Unnamed: 6": "est_male_vet_pop",
                "Unnamed: 7": "male_veteran_crude_rate_per_100K",
                "Unnamed: 8": "male_age_adjusted_rate_per_100K",
                "Unnamed: 9": "female_suicides",
                "Unnamed: 10": "est_female_vet_pop",
                "Unnamed: 11": "female_veteran_crude_rate_per_100K", 
                "Unnamed: 12": "female_age_adjusted_rate_per_100K",
            },
        )
    # drop rows:
    age_adjusted_df = age_adjusted_df.drop([0, 1, 2, 3])

    # drop columns b/c age_adjusted is more applicable than crude rate
    age_adjusted_df = age_adjusted_df.drop(["veteran_crude_rate_per_100K", "male_veteran_crude_rate_per_100K", "female_veteran_crude_rate_per_100K"], axis=1)

    # change column datatypes from 'object' to int64's and floats
    age_adjusted_df = age_adjusted_df.apply(pd.to_numeric)

    # set index to the year
    # age_adjusted_df = age_adjusted_df.set_index("year")

    # splitting data into train and test
    # train, test = train_test_split(age_adjusted_df, train_size=.75, random_state=123)

    # output
    print("Age-Adjusted Veteran Suicide Rate DF")
    print(f"Consists of {len(age_adjusted_df)} rows and {len(age_adjusted_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return age_adjusted_df

# -------------- Age Group DataFrame ----------------

def age_group_df():
    """
    Acquires and preps the second set of data, the 'age_group' DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM/edit?usp=sharing

    sheet2_id = "14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM"

    age_group_df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet2_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns:
    age_group_df = age_group_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "age_group",
                "Unnamed: 2": "total_suicides",
                "Unnamed: 3": "est_total_vet_pop",
                "Unnamed: 4": "veteran_crude_rate_per_100K",
                "Unnamed: 5": "male_suicides",
                "Unnamed: 6": "est_male_vet_pop",
                "Unnamed: 7": "male_veteran_crude_rate_per_100K",
                "Unnamed: 8": "age_group_2",
                "Unnamed: 9": "female_suicides",
                "Unnamed: 10": "est_female_vet_pop",
            },
        )

    # dropping rows
    age_group_df = age_group_df.drop([0, 1, 2, 3])

    # dropping row where age_group == 'Total'
    age_group_df = age_group_df.drop(age_group_df.index[age_group_df.age_group == "Total"])

    # dropping 'age_group_2' column, as it is the same as 'age_group'
    age_group_df = age_group_df.drop(["age_group_2"], axis=1)

    # adding column to enumerate age groups for exploration
    age_group_num = [] 
    for i in age_group_df["age_group"]: 
        if i == "18-34": 
            age_group_num.append(1) 
        elif i == "35-54": 
            age_group_num.append(2) 
        elif i == "55-74":  
            age_group_num.append(3) 
        elif i == "75+":
            age_group_num.append(4)
       
    age_group_df["age_group_num"] = age_group_num

    # imputing '1' where values are '.' so I can convert dtypes to floats and int64's
    age_group_df["female_suicides"] = age_group_df["female_suicides"].replace(".", "1")
    age_group_df["est_female_vet_pop"] = age_group_df["est_female_vet_pop"].replace(".", "1")

    # set index to the year
    # age_group_df = age_group_df.set_index("year", inplace=True)


    # splitting data into train and test
    #train, test = train_test_split(age_group_df, train_size=.75, random_state=123)

    # output
    print("This is the AgeGroup DataFrame")
    print(f"Consists of {len(age_group_df)} rows and {len(age_group_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return age_group_df

# -------------- Recent VHA User DataFrame ----------------

def recent_vha_user():
    """
    Function to import Google Sheet from link into Pandas dataframe
    """
    # original link: https://docs.google.com/spreadsheets/d/10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk/edit?usp=sharing
    
    sheet3_id = "10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk"

    recent_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet3_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns:
    recent_vha_user_df = recent_vha_user_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "vha_suicides",
                "Unnamed: 2": "vha_pop_est",
                "Unnamed: 3": "vha_veteran_crude_per_100K",
                "Unnamed: 4": "vha_age_adjusted_per_100K",
                "Unnamed: 5": "male_suicides",
                "Unnamed: 6": "male_vha_pop_est",
                "Unnamed: 7": "male_vha_veteran_crude_per_100K",
                "Unnamed: 8": "male_vha_age_adjusted_per_100K",
                "Unnamed: 9": "female_suicides",
                "Unnamed: 10": "female_vha_pop_est",
                "Unnamed: 11": "female_vha_veteran_crude_per_100K", 
                "Unnamed: 12": "female_vha_age_adjusted_per_100K",
            },
        )
    
    # drop rows b/c they contain strings that only repeat column names
    recent_vha_user_df = recent_vha_user_df.drop([0, 1, 2, 3])
                        
    # drop crude_per_100K columns because they aren't specific enough
    recent_vha_user_df = recent_vha_user_df.drop(["vha_veteran_crude_per_100K", "male_vha_veteran_crude_per_100K", "female_vha_veteran_crude_per_100K"], axis=1)

    # set index to the year
    # recent_vha_user_df = recent_vha_user_df.set_index("year", inplace=True)


    # change column datatypes from 'object' to int64's and floats
    recent_vha_user_df = recent_vha_user_df.apply(pd.to_numeric)

    # splitting data into train and test
    # train, test = train_test_split(recent_vha_user_df, train_size=.75, random_state=123)

    # output
    print("DataFrame of Suicides Among Recent VHA Users")
    print(f"Consists of {len(recent_vha_user_df)} rows and {len(recent_vha_user_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return recent_vha_user_df

# -------------- VHA By Age Group DataFrame ----------------

def vha_by_age_group():
    """
    Fetches the link and returns the cleaned DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms/edit?usp=sharing
    
    sheet4_id = "11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms"

    vha_by_age_group_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet4_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns:
    vha_by_age_group_df = vha_by_age_group_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "vha_age_group",
                "Unnamed: 2": "vha_suicides",
                "Unnamed: 3": "vha_pop_est",
                "Unnamed: 4": "vha_veteran_crude_per_100K",
            },
        )
    vha_by_age_group_df = vha_by_age_group_df.drop([0, 1, 2, 3])

    # dropping row where vha_age_group == 'Total'
    vha_by_age_group_df = vha_by_age_group_df.drop(vha_by_age_group_df.index[vha_by_age_group_df.vha_age_group == "Total"])

    # assigning group numbers to age groups to get rid of the '-' symbol that keeps me from converting dtypes
    age_group_num = [] 
    for i in vha_by_age_group_df["vha_age_group"]: 
        if i == "18-34": 
            age_group_num.append(1) 
        elif i == "35-54": 
            age_group_num.append(2) 
        elif i == "55-74":  
            age_group_num.append(3) 
        elif i == "75+":
            age_group_num.append(4)
       
    vha_by_age_group_df["vha_age_group_num"] = age_group_num

    # now that the group numbers are assigned, I can drop the 'age_group' column:
    vha_by_age_group_df = vha_by_age_group_df.drop(["vha_age_group"], axis=1)

    # converting dtypes from 'object' to int64s and floats:
    vha_by_age_group_df = vha_by_age_group_df.apply(pd.to_numeric)

    # splitting data into train and test
    # train, test = train_test_split(vha_by_age_group_df, train_size=.75, random_state=123)

    # set index to the year
    # vha_by_age_group_df = vha_by_age_group_df.set_index("year", inplace=True)

    # output
    print("DataFrame of Suicides Among Recent VHA Visits by Age Group")
    print(f"Consists of {len(vha_by_age_group_df)} rows and {len(vha_by_age_group_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return vha_by_age_group_df

# -------------- Non-VHA User DataFrame ----------------

def non_vha_user():
    """
    Fetches and returns cleaned Pandas DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY/edit?usp=sharing

    sheet5_id = "1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY"

    non_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet5_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns:
    non_vha_user_df = non_vha_user_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "non_vha_veteran_suicides",
                "Unnamed: 2": "est_non_vha_pop",
                "Unnamed: 3": "non_vha_crude_per_100K",
                "Unnamed: 4": "non_vha_age_adjusted_per_100K",
                "Unnamed: 5": "male_non_vha_veteran_suicides",
                "Unnamed: 6": "male_non_vha_veteran_pop_est",
                "Unnamed: 7": "male_non_vha_crude_per_100K",
                "Unnamed: 8": "male_non_vha_age_adjusted_per_100K",
                "Unnamed: 9": "female_non_vha_suicides",
                "Unnamed: 10": "female_non_vha_veteran_pop_est",
                "Unnamed: 11": "female_non_vha_crude_per_100K", 
                "Unnamed: 12": "female_non_vha_age_adjusted_per_100K",
            },
        )
    non_vha_user_df = non_vha_user_df.drop([0, 1, 2, 3])

    # drop crude_per_100K columns because they aren't specific enough:
    non_vha_user_df = non_vha_user_df.drop(["non_vha_crude_per_100K", "male_non_vha_crude_per_100K", "female_non_vha_crude_per_100K"], axis=1)

    # convert 'object' dtypes to int64s and floats:
    # non_vha_user_df = non_vha_user_df.apply(pd.to_numeric)

    # set index to the year
    # non_vha_user_df = non_vha_user_df.set_index("year", inplace=True)

    # output
    print("DataFrame of Suicides Among Non-Recent VHA Users")
    print(f"Consists of {len(non_vha_user_df)} rows and {len(non_vha_user_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return non_vha_user_df

# -------------- Non-VHA By Age DataFrame ----------------

def non_vha_by_age():
    """
    Returns cleaned DataFrame of suicide rates by age group of veterans who had not recently visited the VHA.
    """
    # original link: https://docs.google.com/spreadsheets/d/1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg/edit?usp=sharing
    
    sheet6_id = "1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg"

    non_vha_by_age_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet6_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # renaming columns:
    non_vha_by_age_df = non_vha_by_age_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year",
                "Unnamed: 1": "non_user_age_group",
                "Unnamed: 2": "non_vha_veteran_suicides",
                "Unnamed: 3": "non_vha_veteran_pop_est",
                "Unnamed: 4": "non_vha_veteran_crude_per_100K",
            },
        )
    non_vha_by_age_df = non_vha_by_age_df.drop([0, 1, 2, 3])

    # dropping row where age_group == 'Total'
    non_vha_by_age_df = non_vha_by_age_df.drop(non_vha_by_age_df.index[non_vha_by_age_df.non_user_age_group == "Total"])

    # assigning group numbers to age groups to get rid of the '-' symbol that keeps me from converting dtypes
    age_group_num = [] 
    for i in non_vha_by_age_df["non_user_age_group"]: 
        if i == "18-34": 
            age_group_num.append(1) 
        elif i == "35-54": 
            age_group_num.append(2) 
        elif i == "55-74":  
            age_group_num.append(3) 
        elif i == "75+":
            age_group_num.append(4)
       
    non_vha_by_age_df["age_group_num"] = age_group_num

    # now that the group numbers are assigned, I can drop the 'age_group' column:
    non_vha_by_age_df = non_vha_by_age_df.drop(["non_user_age_group"], axis=1)

    # convert dtypes from 'object' to int64s and floats: 
    non_vha_by_age_df = non_vha_by_age_df.apply(pd.to_numeric)

    # splitting data into train and test
    # train, test = train_test_split(non_vha_by_age_df, train_size=.75, random_state=123)

    # set index to the year
    # on_vha_by_age_df = non_vha_by_age_df.set_index("year", inplace=True)

    #output
    print("DataFrame of Suicides Among Those Who Had NOT Recently Visited the VHA")
    print(f"Consists of {len(non_vha_by_age_df)} rows and {len(non_vha_by_age_df.columns)} columns")
    # print("Data has been split into Test and Train portions in separate .py file for exploration.")

    return non_vha_by_age_df

# def split_dataframes():
#     """Simple loop function to split all the dataframes into train, validate, and test sets"""
#     dataframes = age_adjusted_df, age_group_df, recent_vha_user_df, vha_by_age_group, non_vha_user, non_vha_by_age_df

#     for data in dataframes:
#         data_train, data_test = sklearn.model_selection.train_test_split(data_df, train_size=.80, random_state=123)
#         data_train, data_validate = sklearn.model_selection.train_test_split(data_train, train_size=.80, random_state=123)
    
#     return dataframe