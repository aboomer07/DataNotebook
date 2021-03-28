# Script Content:
# Second Data Analytics Project
# Descriptive Analysis of OKCupid Profiles Data
# 1. Meta Analysis: Missing Values etc.
# 2. Basic Descriptive Stats
# 3. Regional Analysis

# Authors: Andrew Boomer, Jacob Pichelmann

# Date: 19.03.2021

#### 0. Setup ####

## import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

## set up paths

# Force the correct directory
if os.getcwd().split("/")[-1] == "CODE":
    os.chdir("..")
curr_dir = os.getcwd()

# If an output directory does not already exist, create one
if not os.path.isdir("OUTPUT"):
    os.mkdir("OUTPUT")
out_dir = curr_dir + "/OUTPUT"


inp_dir = curr_dir + "/DATA/"

## import data

missing_values = ["nan", "-1"]  # account for income missing values = -1
df = pd.read_csv(inp_dir + '3-profiles.csv', na_values=missing_values)


#### 1. Meta Analysis ####

sns.heatmap(df.isnull(), cbar=False)

df.height.min()  # cut of unrealistic values?

#### 2. Basic Descriptive Stats ####

# what does most common man/women in data set look like?
# create helper function that returns most frequent characteristic

def max_freq(col, data = df):
    freq = data[col].value_counts().reset_index()
    freq_max = freq[freq[col] == max(freq[col])]['index'][0]
    return freq_max


males = df[df['sex'] == 'm']
females = df[df['sex'] == 'f']

cols = ['age', 'body_type', 'diet', 'drinks', 'drugs', 'education', 'ethnicity',
        'height', 'income', 'job']

res_male = []
for col in cols:
    res_male.append(max_freq(col, males))

res_female = []
for col in cols:
    res_female.append(max_freq(col, females))

# put results in a table
hybrid = pd.DataFrame({'F': res_female, 'M': res_male})

hybrid




