import pandas as pd
import matplotlib.pyplot as plt

# read datasets into dataframes
daily_report = pd.read_csv('10-02-2022.csv')
covid_confirmed = pd.read_csv('time_series_covid19_confirmed_US(1).csv')
covid_deaths = pd.read_csv('time_series_covid19_deaths_US(1).csv')

# give state with the highest number of deaths
print("State with the highest number of deaths:")
print(daily_report[daily_report['Deaths'] == daily_report['Deaths'].max()]['Province_State'].to_string(index=False))

# give state with the 2nd lowest incident rate
print("State with the 2nd lowest incident rate:")
drop_lowest = daily_report[daily_report['Incident_Rate'] > daily_report['Incident_Rate'].min()]
print(drop_lowest[drop_lowest['Incident_Rate'] == drop_lowest['Incident_Rate'].min()]['Province_State'].to_string(index=False))

# highest and lowest case fatality ratios
print("State with highest case fatality ratio:")
highest_ratio_state = daily_report[daily_report['Case_Fatality_Ratio'] == daily_report['Case_Fatality_Ratio'].max()]
print(highest_ratio_state['Province_State'].to_string(index=False))
print("State with lowest case fatality ratio:")
lowest_ratio_state = daily_report[daily_report['Case_Fatality_Ratio'] == daily_report['Case_Fatality_Ratio'].min()]
print(lowest_ratio_state['Province_State'].to_string(index=False))
print("Difference between case fatality ratios:")
print(float(highest_ratio_state['Case_Fatality_Ratio'])-float(lowest_ratio_state['Case_Fatality_Ratio']))

# find states with the 5 top highest cases
states = []
temp = daily_report
for i in range(0, 5):
    states.append(temp[temp['Confirmed'] == temp['Confirmed'].max()]['Province_State'].to_string(index=False))
    temp = temp[temp['Confirmed'] < temp['Confirmed'].max()]

# plot daily new cases in states with top 5 highest cases
myFig, myAxes = plt.subplots(1, 2, figsize=(10, 5))
cases = []
for state in states:
    cases.append((covid_confirmed[covid_confirmed['Province_State'] == state]['10/4/2022']).sum())
myAxes[0].bar(states, cases)
myAxes[0].set_ylabel("Confirmed Cases")


# plot daily deaths in states with top 5 highest cases
deaths = []
for state in states:
    deaths.append((covid_deaths[covid_deaths['Province_State'] == state]['10/4/2022']).sum())
myAxes[1].bar(states, deaths)
myAxes[1].set_ylabel("Deaths")
plt.show()
