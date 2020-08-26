import pandas as pd
import numpy as np

import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute
from sklearn.model_selection import train_test_split

import suicide_acquire

# def split_age_adjusted_df():
#     """
#     splits age_adjusted df into train, validate, and test portions, leaving 20% for test data
#     """
#     age_adjusted_train, age_adjusted_test = sklearn.model_selection.train_test_split(age_adjusted_df, train_size=.80, random_state=123)
#     age_adjusted_train, age_adjusted_validate = sklearn.model_selection.train_test_split(age_adjusted_train, train_size=.80, random_state=123)

#     return split_age_adjusted_df

# def split_age_group_df():
#     """
#     splits age_group_df into train, validate, and test portions, leaving 20% for test data
#     """
#     age_group_train, age_group_test = sklearn.model_selection.train_test_split(age_group_df, train_size=.80, random_state=123)
#     age_group_train, age_group_validate = sklearn.model_selection.train_test_split(age_group_train, train_size=.80, random_state=123)

#     return split_age_group_df

# def split_recent_vha_user_df():
#     """
#     splits data to leave 20% for test
#     """
#     recent_vha_user_train, recent_vha_user_test = sklearn.model_selection.train_test_split(recent_vha_user_df, train_size=.80, random_state=123)
#     recent_vha_user_train, recent_vha_user_validate = sklearn.model_selection.train_test_split(recent_vha_user_train, train_size=.80, random_state=123)

#     return split_recent_vha_user_df

# def split_vha_by_age_group_df():
#     """
#     splits vha_by_age_group_df to leave 20% for test
#     """

#     vha_by_age_group_train, vha_by_age_group_test = sklearn.model_selection.train_test_split(vha_by_age_group_df, train_size=.80, random_state=123)
#     vha_by_age_group_train, vha_by_age_group_validate = sklearn.model_selection.train_test_split(vha_by_age_group_train, train_size=.80, random_state=123)

#     return split_vha_by_age_group_df

def split_dataframes():
    """Simple loop function to split all the dataframes into train, validate, and test sets"""
    dataframes = age_adjusted_df, age_group_df, recent_vha_user_df, vha_by_age_group, non_vha_user, non_vha_by_age

    for data in dataframes:
        data_train, data_test = sklearn.model_selection.train_test_split(data_df, train_size=.80, random_state=123)
        data_train, data_validate = sklearn.model_selection.train_test_split(data_train, train_size=.80, random_state=123)
    
    return dataframe