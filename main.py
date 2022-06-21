import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as ps
matplotlib.rcParams["figure.figsize"] = (20,10)


complete_org_dataset = ps.read_csv("Bengaluru_House_Data.csv")
#print(complete_org_dataset.head())

#print(complete_org_dataset.iloc[0,:])

# availablity,society`,area_type is not much needed and droping is good idea

complete_org_dataset_afterDropping  =  complete_org_dataset.drop(["area_type" , "availability","society"],axis='columns')
#print(complete_org_dataset_afterDropping.head())

#finding any null values in dataset framework

#print(complete_org_dataset_afterDropping.isnull().sum()) #  it has small null values
# location        1
# size           16
# total_sqft      0
# bath           73
# balcony       609
# price           0

# dropp NA Rows
complete_org_dataset_afterDropping =  complete_org_dataset_afterDropping.dropna()

#print(complete_org_dataset_afterDropping.isnull().sum()) # remomved all na values present in dataset

#print(complete_org_dataset_afterDropping.shape)#(12710 , 6)
#print(complete_org_dataset_afterDropping.size)#76260

# convert 4 bhk , 3 , bhk to seperate Column as BHK and value are 3,4

complete_org_dataset_afterDropping["BHK"] = complete_org_dataset_afterDropping["size"].apply(lambda b: int(b.split(" ")[0]) )
#print(complete_org_dataset_afterDropping.head())
com_org_data_after_bhk = complete_org_dataset_afterDropping.drop(["size"],axis = "columns")
#print(com_org_data_after_bhk.head())

print(com_org_data_after_bhk["balcony"].unique())
print(com_org_data_after_bhk["bath"].unique()) # it shows bathroom like 43 , liiks weird

print(com_org_data_after_bhk[com_org_data_after_bhk.bath>10]) # these are called as outliers

print(com_org_data_after_bhk.total_sqft.unique())
# there are some range values are there , for example 1400 - 1650 . For that please use average , median on both value to single


def convertFloat(x):
    split = x.split("-")
    if len(split)==2:
        return (float(split[0])+float(split[1])/2)
    try:
        return float(x)
    except:
        return None

com_org_data_after_bhk["squarefeet"] = com_org_data_after_bhk["total_sqft"].apply(convertFloat)
com_org_data_after_bhk=com_org_data_after_bhk.drop(["total_sqft"],axis = "columns")

print(com_org_data_after_bhk.squarefeet.isnull().sum())
print(com_org_data_after_bhk.loc[200:225,:])

com_org_data_after_bhk["rate_per_sq_ft"]= round((com_org_data_after_bhk.price*100000 / com_org_data_after_bhk.squarefeet),2)
print(com_org_data_after_bhk.head(10))


print("Values Before  $$$$$$$$$$")
print(com_org_data_after_bhk.location.unique())
#next thing is please check location has 1309 unique values, more dimensio is produced is we go for one got encoding ,
# so please remove less than 10 unique values

import re
def convertLower(word):
    pattern = r'[0-9,]'
    word= re.sub(pattern,"",word)
    word= word.strip()

    return word.lower()


com_org_data_after_bhk["location"] = com_org_data_after_bhk["location"].apply(convertLower)
print("Values after $$$$$$$$$$")
print(com_org_data_after_bhk.location.unique())

#check out maximum use case of location

location_used = com_org_data_after_bhk.groupby('location')["location"].agg('count').sort_values(ascending = False)

less_used_location = location_used[location_used<10 ]
print("info :",less_used_location)
print("Descibe :",com_org_data_after_bhk.describe())
#category all small values in to single column -->other
print((com_org_data_after_bhk["squarefeet"]<500))

com_org_data_after_bhk = com_org_data_after_bhk.location.apply( lambda x:"other" if x in less_used_location else x)

com_org_data = com_org_data_after_bhk[ ~(com_org_data_after_bhk['squarefeet']<400)]



#for k,v in com_org_data_after_bhk.groupby('location'):
#    print(v)
#print(com_org_data_after_bhk.groupby('location'))

# Removing outliers in same area , if rajaji nagar 1 value is 100 , then other is 1200 please remove both of not match b/w std

def removeOutliers(df):
    df_out = ps.DataFrame()

    for key , value in df.groupby('location'):
        mean =  np.mean(value["rate_per_sq_ft"])
        std = np.std(value["rate_per_sq_ft"])
        reduced_df = value[(value.rate_per_sq_ft >(mean-std) ) &  (value.rate_per_sq_ft >(mean+std))]
        df_out= ps.concat((df_out,reduced_df),ignore_index=True)

    return df_out

new_Dataset = removeOutliers(com_org_data )

print(new_Dataset.shape)


