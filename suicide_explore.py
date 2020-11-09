import pandas as pd
import numpy as np
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

##VIMP: I NEED TO TAKE ALL THE DATA IN THE FUNCTION BELOW AND APPLY IT TO EACH INDIVIDUAL, CLEANED DATAFRAME.  CANNOT LUMP ONE FUNCTION INTO WHOLE PRGRAM!!

## Function to split the DataFrames into Train, Validate, and Test, then print the proof it's been done

# Base Function:
def data_split(df):
    """
    This function takes the df parameter, splits it into train, validate, and test portions, then prints out to the user the proof that it has been done in accordance with the 20-25% recommended data split
    """

    # do the split
    train, test = sklearn.model_selection.train_test_split(df, train_size=.80, random_state=123)
    train, validate = sklearn.model_selection.train_test_split(train, train_size=.80, random_state=123)

    # printout to verify split has occured
    for data in df:
        print(f"Trained df has {len(train)} rows and {len(train.columns)} columns" )
        print(f"Validated df has {len(validate)} rows and {len(validate.columns)} columns")
    # # print trained dataframe
    # print(f"Trained {df} DataFrame")
    # print(f"Consists of {len(train)} rows and {len(train.columns)} columns")

    # # print validated dataframe
    # print(f"Validated {df} DataFrame")
    # print(f"Consists of {len(validate)} rows and {len(validate.columns)} columns")

    return df

# def split_age_adjust(age_adjusted_df):
#     """
#     This function splits the age_adjusted_df into train, validate, and test portions, then prints out to the user the proof that it has been done in accordance with the 20-25% recommended data split
#     """

#     train, test = sklearn.model_selection.train_test_split(df, train_size=.80, random_state=123)
#     train, validate = sklearn.model_selection.train_test_split(train, train_size=.80, random_state=123)
