import pandas as pd

# read file into dataframe and print
frame = pd.read_csv('mtcars.csv')
print(frame)

# set index of dataframe to Car Name and print
frame = frame.set_index('Car Name')
print(frame)
