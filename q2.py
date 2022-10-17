import pandas as pd

# read csv using specific columns and car name as index
frame = pd.read_csv('mtcars.csv', usecols=['Car Name', 'cyl', 'gear', 'hp', 'mpg'])
frame = frame.set_index('Car Name')
frame = frame.rename(columns={'cyl': 'Cylinders', 'gear': 'Gear', 'hp': 'Horsepower', 'mpg': 'Miles per Gallon'})

# reorder columns and print
frame.insert(0, 'Miles per Gallon', frame.pop('Miles per Gallon'))
frame.insert(0, 'Horsepower', frame.pop('Horsepower'))
frame.insert(0, 'Gear', frame.pop('Gear'))
frame.insert(0, 'Cylinders', frame.pop('Cylinders'))
print(frame)

# add Powerful column and print
powerful = []
for i in frame.itertuples():
    if i[3] >= 110:
        powerful.append(True)
    else:
        powerful.append(False)
frame['Powerful'] = powerful
print(frame)

# print dataframe with Horsepower deleted
print(frame.drop('Horsepower', axis=1))

# list cars with mph>25 and sort in descending order of horsepower
print(frame[frame['Miles per Gallon'] > 25.0].sort_values(by='Horsepower', ascending=False))

# filter to car that is powerful and has the highest mpg
powerful_cars = frame[frame["Powerful"] == True]
print(powerful_cars[powerful_cars['Miles per Gallon'] == powerful_cars['Miles per Gallon'].max()])
