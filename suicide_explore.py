import pandas as pd
import numpy as np
import sklearn.preprocessing
import sklearn.model_selection
import sklearn.impute
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

##VIMP: I NEED TO TAKE ALL THE DATA IN THE FUNCTION BELOW AND APPLY IT TO EACH INDIVIDUAL, CLEANED DATAFRAME.  CANNOT LUMP ONE FUNCTION INTO WHOLE PRGRAM!!

## Function to split the DataFrames into Train, Validate, and Test, then print the proof it's been done

def data_split(df):
    """
    This function takes the df parameter, splits it into train, validate, and test portions, then prints out to the user the proof that it has been done in accordance with the 20-25% recommended data split
    """

# do the split
train, test = sklearn.model_selection.train_test_split(df, train_size=.80, random_state=123)
train, validate = sklearn.model_selection.train_test_split(train, train_size=.80, random_state=123)

# print trained dataframe
print(f"Trained {df.title()} DataFrame")
print(f"Consists of {len(train)} rows and {len(train.columns)} columns")

train.head()

# print validated dataframe
print(f"Validated {df.title()} DataFrame")
print(f"Consists of {len(validate)} rows and {len(validate.columns)} columns")

validate.head()

