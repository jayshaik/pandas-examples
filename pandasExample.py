#!/usr/bin/env python

"""
I wrote this for myself as a demo after being inspired by
https://www.youtube.com/watch?v=e60ItwlZTKM&feature=youtu.be&ab_channel=JoeJames (nice video with good examples).
Some code from his video pasted here for my reference (since there were
many good examples).
Data taken from https://github.com/joeyajames/Python/blob/master/Pandas/Fremont_weather.txt
@joeyajames thanks!

As I look back on this, I realize it's quite rudimentary but shows some simple
examples for those new to pandas.
"""

import numpy as np
import pandas as pd

df = pd.read_csv("Freemont_weather.txt")
df.head()
df.tail()
df.dtypes
df.columns
df.values
df.index
df.describe()
df.info()

# select * from df order by avg_low DESC
# sort dataframe by a given column

# This return a DataFrame
#
df.sort_values('avg_low', ascending=False)

# This returns a Series.
#
df.avg_low.sort_values(ascending=False)

# Show just one column.
df['avg_low']

# The second parameter (columns) is omitted which means all columns.
# The rows 4:7 are returned.
#
df[4:7]

# Rows parameter is omitted (columns are a list), so get these 3 columns
# but all rows.
#
df[['month','avg_low', 'avg_high']]

# Get all rows and two columns: months and avg_low.
#
df.loc[:,['month','avg_low']]

# Get columns 8:11 and two rows: months, ave_high.
#
df.loc[8:11,['month','avg_high']]
df.loc[10:12,['month','avg_precipitation']]

# Get the scalar value of month on row 9.
#
df.loc[9, 'month']

# The iloc method gets rows/columns by index.
# Get the 3:5 slice of rows, and columns 0:4.
#
df.iloc[3:5,0:4]

# Get a single column of values; returns a Series.
# select avg_precipitation
df.avg_precipitation

# select record_high from df
df.record_high

# Use bracket operator to get rows where a boolean is True.
# Returns a DataFrame.
# select * from df where avg_precipitation > 1
#
df[df.avg_precipitation > 1.0]

# select * from df where record_high < 80
df[df.record_high < 80]

# Inside the brackets yields some kind of datastructure (like vector of booleans)
# that is used with the bracket operator
df.record_high < 80

# Get the month column.
# Generates a series.
# These two return the same thing:
df['month']
df.month

# Get the month column where the month is in a given list of months
# Generates a Series of booleans
df['month'].isin(["Jun", "May", "Oct"])

# Take that Series of booleans and use the bracket operator
df[df['month'].isin(["Jun", "May", "Oct"])]
t = df[df['month'].isin(["Jun", "May", "Oct"])]

# This yields the same result but might be more useful in code.
#
tt = df[df['month'].isin(["Jun", "May", "Oct"])]
df[tt]

# Assign single value to cell
# Assign the avg_precipitation of the 9th row to 102.3
#
df.loc[9, ['avg_precipitation']] = 102.3

# Assigns to nan (not a number); nan values are skipped in calculations
#
df.loc[9, ['avg_precipitation']] = np.nan

# Number of rows in a DataFrame
len(df)

# numpy array of 5 the size of the number of rows in df
np.array([5] * len(df))

# Assign the avg_low column to all 5s
df.loc[:,'avg_low'] = np.array([5] * len(df))

# Add two columns (returns a series)
# Divide the series by 2.
# Assign a series to a newly created column using the bracket operator
df['avg_day'] = (df.avg_high + df.avg_low) / 2
