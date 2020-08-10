import pandas as pd
import numpy as np

def recent_vha_user():
    """
    Function to import Google Sheet from link into Pandas dataframe
    """
    # original link: https://docs.google.com/spreadsheets/d/10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk/edit?usp=sharing
    
    sheet3_id = "10DYv7ylkz9_xcitXbSzJiZvUITaz-xH6SOky1CGjshk"

    recent_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet3_id}/export?format=csv")

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
    recent_vha_user_df = recent_vha_user_df.drop([0, 1, 2, 3])

    print("DataFrame of Suicides Among Recent VHA Users")

    return recent_vha_user_df

def by_age_group():
    """
    Fetches the link and returns the cleaned DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms/edit?usp=sharing
    
    sheet4_id = "11HNhevau7bHyvflftnqxTKzEA2sME60z_1H3zPQHrms"

    by_age_group_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet4_id}/export?format=csv")

    pd.set_option("display.max_columns", None)

    by_age_group_df = by_age_group_df.rename(
            columns={
                "2005-2017 National Suicide Data Appendix": "year_of_death",
                "Unnamed: 1": "age_group",
                "Unnamed: 2": "vha_veteran_suicides",
                "Unnamed: 3": "vha_veteran_pop_est",
                "Unnamed: 4": "vha_veteran_crude_per_100K",
            },
        )
    by_age_group_df = by_age_group_df.drop([0, 1, 2, 3])

    print("DataFrame of Suicides Among Recent VHA Visits by Age Group")

    return by_age_group_df

def non_vha_user():
    """
    Fetches and returns cleaned Pandas DataFrame
    """
    # original link: https://docs.google.com/spreadsheets/d/1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY/edit?usp=sharing

    sheet5_id = "1LAAgkTWJK6yYHq8SbSMHogP7kS_7V-kNlQ-FyoYrRXY"

    non_vha_user_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet5_id}/export?format=csv")

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

    print("DataFrame of Suicides Among Non-Recent VHA Users")

    return non_vha_user_df

def non_vha_by_age():
    """
    Returns cleaned DataFrame of suicide rates by age group of veterans who had not recently visited the VHA.
    """
    # original link: https://docs.google.com/spreadsheets/d/1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg/edit?usp=sharing
    
    sheet6_id = "1KshDEv1WSQmfmwhbIs7az7dzVFczzx1CxEZ5Hx1Rfrg"

    non_vha_by_age_df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet6_id}/export?format=csv")

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

    print("DataFrame of Suicides Among Those Who Had NOT Recently Visited the VHA")

    return non_vha_by_age_df


# sheet2_id = "14okhBqlMF8MFoaLy0HM9StT_brUx3kUvSXDvCRqcIxM"

# age_group_df= pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet2_id}/export?format=csv")

# pd.set_option("display.max_columns", None)

# print("This is the AgeGroup DataFrame")

# age_group_df