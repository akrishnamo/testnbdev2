# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_mtables.ipynb.

# %% auto 0
__all__ = ['table', 'read_csv']

# %% ../nbs/00_mtables.ipynb 4
import pandas as pd        
import numpy as np 
from urllib.error import URLError

# %% ../nbs/00_mtables.ipynb 6
def table(n: int, # a number for which you want multiplication tables
         ):
    for i in range(1,11,1):
        print(f"{n} times {i} = {n*i}")

# %% ../nbs/00_mtables.ipynb 9
def read_csv(file:str, # file path
             col_dict:dict, # dictionary with column name  as keys  and  dtypes  as  values
            )-> tuple: # a pandas dataframe and an  error list
    """
    This function read_csv  helps you to read a csv file with given  columns  only,
    additionally converts into given data types.
    
    Inputs:
        file -----------> file path.
        
        col_dict -----------> dictionary with column name  as keys  and  dtypes  as  values, 
                              ex:d={"colmn_name":float,"colmn_name":int} ,for date {"colmn_name":("date","%Y-%m-%d")}.
                              Note: date  is an special case need to pass a tuple with key "date" and format.
    Output:
         function returns pandas dataframe if no errors found,
         
         function returns list of errors if errors found
         
    """
    errors=[]
    emptydf=pd.DataFrame()
    
    #first set of checks on file missing, corrupted, etc.
    try:
        df=pd.read_csv(file)
    except FileNotFoundError as e:
        errors.append("File not found please check file path, Error: "+str(e))
        return emptydf, errors
    except URLError as e1:
        errors.append('URL not found, Error: '+str(e1))
        return emptydf, errors
    except UnicodeDecodeError as e2:
        errors.append("corrupted data or not a csv file, Error:  "+str(e2))
        return emptydf, errors
    
    #second set of checks
    try:
        df=df[list(col_dict.keys())]
    except KeyError as e3:
        errors.append("key error columns not found, Error: " + str(e3))
        return emptydf, errors

    for k,v in col_dict.items():
        if type(v)== tuple:
            try:
                df[k]=pd.to_datetime( df[k],format=v[1])
            except ValueError as e4: 
                errors.append("Wrong date format , Error:  "+str(e4))
                return emptydf, errors
        else:
            try:
                df[k]= df[k].astype(v)
            except KeyError as e5:
                errors.append("key error columns  not found, Error:  "+str(e5) )
                return emptydf, errors
    return df, errors
