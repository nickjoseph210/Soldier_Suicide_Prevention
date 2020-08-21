import pandas as pd
import numpy as np

# Google Sheet imports are tagged with the following keyword arguments: sep=None, thousands=",", and engine="python"
# This was in an effort to import the spreadsheet data without having to go back in and remove / replace commas and spaces
# with either regex or python commands.

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
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "veteran_suicide_deaths",
                "Unnamed: 2": "veteran_population_estimate",
                "Unnamed: 3": "veteran_crude_rate_per_100K",
                "Unnamed: 4": "veteran_age_adjusted_rate_per_100K",
                "Unnamed: 5": "male_veteran_suicide_deaths",
                "Unnamed: 6": "male_veteran_population_estimate",
                "Unnamed: 7": "male_veteran_crude_rate_per_100K",
                "Unnamed: 8": "male_veteran_age_adjusted_rate_per_100K",
                "Unnamed: 9": "female_veteran_suicide_deaths",
                "Unnamed: 10": "female_veteran_population_estimate",
                "Unnamed: 11": "female_veteran_crude_rate_per_100K", 
                "Unnamed: 12": "female_veteran_age_adjusted_rate_per_100K",
            },
        )
    # drop rows:

    age_adjusted_df = age_adjusted_df.drop([0, 1, 2, 3])

    # drop columns b/c age_adjusted is more applicable than crude rate

    age_adjusted_df = age_adjusted_df.drop(["veteran_crude_rate_per_100K", "male_veteran_crude_rate_per_100K", "female_veteran_crude_rate_per_100K"], axis=1)

    print("This is the Age-Adjusted Veteran Suicide Rate DF")

    return age_adjusted_df

def age_group_df():
    """
    Acquires and preps the second set of data, the 'age_group' DataFrame
    """
    # https://docs.google.com/spreadsheets/d/14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM/edit?usp=sharing

    sheet2_id = "14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM"

    age_group_df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet2_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    # Renaming Columns

    age_group_df = age_group_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "age_group",
                "Unnamed: 2": "veteran_suicide_deaths",
                "Unnamed: 3": "veteran_population_estimate",
                "Unnamed: 4": "veteran_crude_rate_per_100K",
                "Unnamed: 5": "male_veteran_suicide_deaths",
                "Unnamed: 6": "male_veteran_population_estimate",
                "Unnamed: 7": "male_veteran_crude_rate_per_100K",
                "Unnamed: 8": "age_group_2",
                "Unnamed: 9": "female_veteran_suicide_deaths",
                "Unnamed: 10": "female_veteran_population_estimate",
            },
        )

    # Dropping Rows

    age_group_df = age_group_df.drop([0, 1, 2, 3])

    # dropping row where age_group == 'Total'

    age_group_df = age_group_df.drop(age_group_df.index[age_group_df.age_group == "Total"])

    # dropping 'age_group_2' column, as it is the same as 'age_group'

    age_group_df = age_group_df.drop(["age_group_2"], axis=1)

    # Adding column to enumerate age groups for exploration

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


    print("This is the AgeGroup DataFrame")

    return age_group_df

def recent_vha_user():
    """
    Function to import Google Sheet from link into Pandas dataframe
    """
    # original link: https://docs.google.com/spreadsheets/d/10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk/edit?usp=sharing
    
    sheet3_id = "10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk"

    recent_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet3_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    recent_vha_user_df = recent_vha_user_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "vha_veteran_suicides",
                "Unnamed: 2": "vha_veteran_pop_est",
                "Unnamed: 3": "vha_veteran_crude_per_100K",
                "Unnamed: 4": "vha_veteran_age_adjusted_per_100K",
                "Unnamed: 5": "male_vha_veteran_suicides",
                "Unnamed: 6": "male_vha_veteran_pop_est",
                "Unnamed: 7": "male_vha_veteran_crude_per_100K",
                "Unnamed: 8": "male_vha_veteran_age_adjusted_per_100K",
                "Unnamed: 9": "female_vha_veteran_suicides",
                "Unnamed: 10": "female_vha_veteran_pop_est",
                "Unnamed: 11": "female_vha_veteran_crude_per_100K", 
                "Unnamed: 12": "female_vha_veteran_age_adjusted_per_100K",
            },
        )
    
    # drop rows b/c they contain strings that only repeat column names
    recent_vha_user_df = recent_vha_user_df.drop([0, 1, 2, 3])
                        
    # drop crude_per_100K columns because they aren't specific enough
    recent_vha_user_df = recent_vha_user_df.drop(["vha_veteran_crude_per_100K", "male_vha_veteran_crude_per_100K", "female_vha_veteran_crude_per_100K"], axis=1)
    
    print("DataFrame of Suicides Among Recent VHA Users")

    return recent_vha_user_df

def vha_by_age_group():
    """
    Fetches the link and returns the cleaned DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms/edit?usp=sharing
    
    sheet4_id = "11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms"

    vha_by_age_group_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet4_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    vha_by_age_group_df = vha_by_age_group_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "age_group",
                "Unnamed: 2": "vha_veteran_suicides",
                "Unnamed: 3": "vha_veteran_pop_est",
                "Unnamed: 4": "vha_veteran_crude_per_100K",
            },
        )
    vha_by_age_group_df = vha_by_age_group_df.drop([0, 1, 2, 3])

    # dropping row where age_group == 'Total'

    vha_by_age_group_df = vha_by_age_group_df.drop(vha_by_age_group_df.index[vha_by_age_group_df.age_group == "Total"])

    print("DataFrame of Suicides Among Recent VHA Visits by Age Group")

    return vha_by_age_group_df

def non_vha_user():
    """
    Fetches and returns cleaned Pandas DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY/edit?usp=sharing

    sheet5_id = "1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY"

    non_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet5_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    non_vha_user_df = non_vha_user_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
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

    # drop crude_per_100K columns because they aren't specific enough
    non_vha_user_df = non_vha_user_df.drop(["non_vha_crude_per_100K", "male_non_vha_crude_per_100K", "female_non_vha_crude_per_100K"], axis=1)

    print("DataFrame of Suicides Among Non-Recent VHA Users")

    return non_vha_user_df

def non_vha_by_age():
    """
    Returns cleaned DataFrame of suicide rates by age group of veterans who had not recently visited the VHA.
    """
    # original link: https://docs.google.com/spreadsheets/d/1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg/edit?usp=sharing
    
    sheet6_id = "1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg"

    non_vha_by_age_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet6_id}/export?format=csv", sep=None, thousands=",", engine="python")

    pd.set_option("display.max_columns", None)

    non_vha_by_age_df = non_vha_by_age_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "non_user_age_group",
                "Unnamed: 2": "non_vha_veteran_suicides",
                "Unnamed: 3": "non_vha_veteran_pop_est",
                "Unnamed: 4": "non_vha_veteran_crude_per_100K",
            },
        )
    non_vha_by_age_df = non_vha_by_age_df.drop([0, 1, 2, 3])

    # dropping row where age_group == 'Total'

    non_vha_by_age_df = non_vha_by_age_df.drop(non_vha_by_age_df.index[non_vha_by_age_df.non_user_age_group == "Total"])

    print("DataFrame of Suicides Among Those Who Had NOT Recently Visited the VHA")

    return non_vha_by_age_df


# sheet2_id = "14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM"

# age_group_df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet2_id}/export?format=csv")

# pd.set_option("display.max_columns", None)

# print("This is the AgeGroup DataFrame")

# age_group_df