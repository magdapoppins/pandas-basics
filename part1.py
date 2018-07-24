# F9 to execute! <3 
import pandas as pd

# Define where our data is - capitals for constant values!
# Windows is reeeeally picky with getting the whole path, typed exactly like this...
CSV_PATH = "C:\\Samples\\PandasBasics\\artworkdata.csv"

# Read the first 5 rows to check we got it right
# Open variable explorer in the second little window
# Click on DataFrame in the Type column to get a better picture!
df = pd.read_csv(CSV_PATH, nrows=5)

# Get rid of the extra index, use the datasets own id column instead
# And specify which columns we want
df = pd.read_csv(CSV_PATH, 
                 nrows=5, 
                 index_col='id')

# Specify columns to use
COLS_TO_USE = ['id', 'artist', 
               'title', 'medium', 
               'year', 'acquisitionYear', 
               'height', 'width', 'units']

df = pd.read_csv(CSV_PATH,
                 index_col='id',
                 usecols=COLS_TO_USE)

# Running this will give a warning about -- have mixed types. 
# This is due to unclean data - we'll fix it later.
df.to_pickle("C:\\Samples\\PandasBasics\\artists.pickle")



