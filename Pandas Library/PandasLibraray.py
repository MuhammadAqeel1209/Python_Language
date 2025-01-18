#Import all libiraries 👇👇
import pandas as pd
import numpy as np 
from pandas.tseries.holiday import USFederalHolidayCalendar
from pandas.tseries.offsets import CustomBusinessDay

 #Dictonary 👇👇
dict1 = {
    "Name":["Aqeel","Ali","Arooba","Amna"],
    "Marks":[92,45,67,89],
    "City" :["Faisalabad","Lahore","Karachi","Islamabad"]
}

#Making Data Frame of Dictionary 👇👇
df = pd.DataFrame(dict1) #Data Frame -->Two Dimensional Array -->Tabular Spread Sheets Like structre which contain Row and Column
# print(df)
filter  = df.Marks > 50    # --> Filter the data 
# print(df[filter])

# print(df.iat[2,2])       # --> iat function
# print(df.at[2,'Marks'])  # --> at function


df.to_csv("Data.csv") # 👈👈 Make Excel Sheets with index
df.to_csv("Data_Index.csv",index=False) # 👈👈Make Excel Sheets with out index

# print(df.head(2))    #  👈👈 Show Start Some Rows
# print(df.tail(2))    # 👈👈  Show Last Some  Rows
# print(df.describe()) # 👈👈 Perfrom Some Mathematical Operation on data frame which is follow as 👉👉 count,mean,std,min,25%,50%,75%,max
Aqeel = pd.read_csv('Aqeel.csv')
# print(Aqeel)
# Aqeel['Speed'][0] = 50  # 👈👈 Change Value on single index
# print(Aqeel['Speed'])   # 👈👈 Display Single Column
#Aqeel.to_csv('Aqeel.csv')# 👈👈 Make Excel Sheets

ser = pd.Series(np.random.rand(35)) # 👈👈 Make Series --> One Dimensional Array with index. it store a single row or column in data frame
#print(ser)
# print(type(ser)) # 👈👈 Check Type of serires

dataFrame = pd.DataFrame(np.random.rand(334,5),index=np.arange(334))

#print(dataFrame.head())        #  👈👈 Show Start Some Rows
# print(dataFrame.tail())       #  👈👈 Show Start Some Rows
# print(type(dataFrame))        # 👈👈 Check Type of data frame
#print(dataFrame.describe())    # 👈👈 Perfrom Some Mathematical Operation on data frame which is follow as 👉👉 count,mean,std,min,25%,50%,75%,max
#print(dataFrame.index)         # 👈👈 In the form of Row 
#print(dataFrame.columns)       # 👈👈 In the form of Col
#print(dataFrame)
# print(dataFrame.to_numpy())   # 👈👈 Convert To Numpy Array
#print(dataFrame.T)             # 👈👈 Tarnspose
#print(dataFrame.sort_index(axis= 0,ascending=False)) # 👈👈 Axis = 0 == Row
#print(dataFrame.sort_index(axis= 1,ascending=False)) # 👈👈 Axis = 1 == Col
dataFrame.columns = list("ABCDE")     # 👈👈Convert the column name from NUMBER  TO ALPHABETS
#print(dataFrame)
#print(dataFrame.loc[[1,2],['C','D']])# 👈👈 Specific Column Display
#Importnat Note 👇👇👇
    #1)Loc 👉👉 Work on column name and row name
    #2)Iloc 👉👉 Work on Column Index and Row Index 
# print(dataFrame.iloc[1,4])         # 👈👈 Specific Value on the two dimensional element
# print(dataFrame.iloc[[0,1],[1,2]]) # 👈👈 Specific Column
# print(dataFrame)
# print(dataFrame.drop([0,3],inplace=True))     # 👈👈 using inplace delete permanentaly and make change in same data frame directly #  By default axis = 0 # For Delete the row
# dataFrame.reset_index(drop=True,inplace=True) # 👈👈 Reset the index after delete some data permanentaly
# print(dataFrame)
#print(dataFrame[3].isnull())   # 👈👈 When column have some value show false(not null)
#dataFrame.loc[:,[3]] = None    # 👈👈Set the value ny using loc #All value in column 3 make none
#print(dataFrame[3].isnull())   # 👈👈When column have not value show true(null)
# print(dataFrame)
df = pd.DataFrame({"name": ['Alfred', 'Batman', 'Alfred'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})
#print(df.dropna())               # 👈👈 Drop the rows where at least one element is missing.
#print(df.dropna(how="all"))      # 👈👈 Drop the rows where all elements are missing.
#print(df.dropna(axis='columns')) # 👈👈 Drop the columns where at least one element is missing.
# print(df.drop_duplicates())     # 👈👈 Remove Duplicate items
# print(df.drop_duplicates(subset=['name'],keep='first')) # 👈👈 To remove duplicates and keep by default first occurrences #By default, it removes duplicate rows based on all columns.
# print(df.drop_duplicates(subset=['name'],keep='last'))  # 👈👈 To remove duplicates and keep last occurrences
# print(df.drop_duplicates(subset=['name'],keep= False))  # 👈👈 Drop all duplicates.
# print(df.shape)   # 👈👈 Shape
# print(df.info())  # 👈👈 info about DataFrame
# print(df['name'].value_counts())              # 👈👈 Give Count Of unique Value
#print(df['toy'].value_counts(dropna=False))    # 👈👈 Give Count Of unique Value and show dropna value
# print(df['born'].value_counts(dropna=False))  # 👈👈 Give Count Of unique Value and show dropna value
# print(df.notnull()) # we use also isnull      # 👈👈 Check Null Or Not

#-------------Make Data Frame using Different Type-----------------------
# 1)Make DataFrame Using Dictionary 
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
# print(df)

# 2)Make DataFrame Using Tuple List
weather_data = [
    ('1/1/2017',32,6,'Rain'),
    ('1/2/2017',35,7,'Sunny'),
    ('1/3/2017',28,2,'Snow')
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
# print(df)

# 3)Using list of dictionaries
weather_data = [
    {'day': '1/1/2017', 'temperature': 32, 'windspeed': 6, 'event': 'Rain'},
    {'day': '1/2/2017', 'temperature': 35, 'windspeed': 7, 'event': 'Sunny'},
    {'day': '1/3/2017', 'temperature': 28, 'windspeed': 2, 'event': 'Snow'},
    
]
df = pd.DataFrame(data=weather_data, columns=['day','temperature','windspeed','event'])
# print(df)

#--------------------------------------------------------------------
wdf = pd.read_csv('weather_data.csv',parse_dates=['day'])
# print(wdf)
# new_df = wdf.fillna({
#     "temperature" : 0,
#     "windspeed" : 0,
#     "event" : "no-event"
# })

# new_df = wdf.fillna(method='ffill') # ffill --> forward fill  Fill the value where no value fill
new_df = wdf.fillna(method='bfill') # ffill --> backward fill  Fill the value where no value fill

# print(wdf.dropna()) # Drop all the colum where one row be contain Nan
# print(wdf.dropna(thresh = 2)) # Drop all the colum where one row be contain Nan thresh mean which row how many Nan

# print(new_df)

city_df = pd.read_csv("weather_by_cities.csv")
# print(city_df)

#------------------------Groupby Method --------------------------
city_gr = city_df.groupby('city')

# Calling the Group method and data frame convert in to 👇👇👇 to the process of for loop where we print 

# Calling group method and covert to that for loop process
# for city, new_city_df in city_gr:
#     print(city)
#     print(new_city_df)

# print(city_gr.get_group('mumbai'))

# print(city_gr.max())
# print(city_gr.min())
# print(city_gr.mean())
# print(city_gr.describe())


#------------------------------Concat Method--------------------------------
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})
# print(india_weather)

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})
# print(us_weather)

# df = pd.concat([india_weather, us_weather]) # Concat used to merge to difference data frame
# df = pd.concat([india_weather, us_weather],ignore_index=True) # Concat used to merge to difference data frame
df = pd.concat([india_weather, us_weather],keys=['india','us']) # Concat used to merge to difference data frame

# print(df) 

#-----------------------Merge Tutorial-------------------------
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})

df3 = pd.merge(df1, df2, on="city")
# print(df3)

#-----------------------Joining Tutorial-------------------------
join_one = pd.DataFrame({
    "city": ["new york","chicago","orlando", "baltimore"],
    "temperature": [21,14,35, 38],
})

join_two = pd.DataFrame({
    "city": ["chicago","new york","san diego"],
    "humidity": [65,68,71],
})

# final_join =pd.merge(join_one,join_two,on="city",how="inner") # inner Join
# final_join =pd.merge(join_one,join_two,on="city",how="outer") # Outter Join
# final_join =pd.merge(join_one,join_two,on="city",how="left") # left Join 
# final_join = pd.merge(join_one,join_two,on="city",how="right") # Right join
# print(final_join)

#-----------------------Pivot Tutorial-------------------------
df = pd.read_csv("weather.csv")
# print(df.pivot(index='city',columns='date'))
# print(df.pivot_table(index="city",columns="date", margins=True,aggfunc=np.sum))

#-----------------------Grouper Function-------------------------
weather_df = pd.read_csv("weather3.csv")
# weather_df['date'] = pd.to_datetime(weather_df['date'])
# print(weather_df.pivot_table(index=pd.Grouper(freq='M',key='date'),columns='city'))


#-----------------------Melt Function-------------------------
# melt() function is useful to massage a DataFrame into a format where one or more columns are identifier variables, while all other columns, considered measured variables, are unpivoted to the row axis, leaving just two non-identifier columns, variable and value
data = pd.read_csv('weatherdata.csv')
# print(data)
# data = pd.melt(data,id_vars=["day"])
# data = data[data['variable'] == 'chicago'] #Show only one city using varaible method
data = pd.melt(data,id_vars=["day"],var_name="City",value_name="Temperature") # 👈 👈Set Varaible name and value same as this way 
# print(data)

#-----------------------Stack And Unstack Function-------------------------
excel = pd.read_excel('stocks.xlsx',header=[0,1])
stack = excel.stack()
# print(stack)

unstack = stack.unstack()
# print(unstack)


#-----------------------Cross Tab Function-------------------------
survey = pd.read_excel('survey.xls')
# print(survey)

# crosssurvey = pd.crosstab(survey.Nationality,survey.Handedness)
crosssurvey = pd.crosstab(survey.Sex,[survey.Handedness,survey.Nationality],margins=True)
# crosssurvey = pd.crosstab(survey.Sex,survey.Handedness,margins=True)
# print(crosssurvey)


#-----------------------DateTime index Tutorials-------------------------
# appl = pd.read_csv('aapl.csv')
appl = pd.read_csv('aapl.csv',parse_dates=["Date"],index_col="Date") # Here we convert the date from str to date and index make the date column
# print(appl)
# print(type(appl.Date[0]))
# print(appl.index)
# print(appl["2017-01"].Close.mean()) # 👈👈👈<-- Find the mean only "Close" Column
# print(appl.asfreq('M',method='pad'))

USAFreq = CustomBusinessDay(calendar=USFederalHolidayCalendar())
# print(pd.date_range(start="7/1/2017",end="7/21/2017",freq=USAFreq))

week = CustomBusinessDay(weekmask = "Sun Mon Tue Wed Thu")

# print(pd.date_range(start="7/1/2017",end="7/29/2017",freq=week)) #That Show those date of Sun Mon Tue Wed Thu



#----------------------- Resample Tutorials-------------------------
# Resample -- used to find the frequency monthly weekly Quater
# print(appl.Close.resample('M').mean()) # Here M -- Month W -- Week Q -- Quater


#----------------------- Period Tutorials-------------------------
y = pd.Period("2016") #create Year Period
# print(dir(y))
# print(y.start_time)
# print(y.end_time)

month = pd.Period('2011-1',freq="M") #Create Month Period
# print(month)
# print(month.start_time)
# print(month.end_time)

# day = pd.Period("2017-02-28",freq="D") #Create Daily Period
# print(day)

hours = pd.Period("2017-02-28 23:00:00",freq="H")# Create Hourly Period
# print(hours)
# print(hours.start_time)
# print(hours.end_time)