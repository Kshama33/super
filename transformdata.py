import pandas as pd

flightlog = 'Airline Code;DelayTimes;FlightCodes;To_From\nAir Canada (!);[21, 40];20015.0;WAterLoo_NEWYork\n<Air France> (12);[];;Montreal_TORONTO\n(Porter Airways. );[60, 22, 87];20035.0;CALgary_Ottawa\n12. Air France;[78, 66];;Ottawa_VANcouvER\n""".\\.Lufthansa.\\.""";[12, 33];20055.0;london_MONTreal\n'

table = pd.DataFrame([i.split(";") for i in flightlog.split("\n")][1:],columns=["Airline Code", "DelayTimes", "FlightCodes","To_From"])
table['FlightCodes'].fillna(method='ffill', inplace=True)
table['FlightCodes'] = pd.to_numeric(table['FlightCodes'],errors='coerce', downcast='integer')
for i in range(1, table.shape[0]):
    if pd.isna(table.loc[i, 'FlightCodes']):
        table.loc[i, 'FlightCodes'] = table.loc[i-1, 'FlightCodes'] + 10
table['FlightCodes'] = table['FlightCodes'].astype(int)
table[['To', 'From']] = table['To_From'].str.split('_', expand=True)
table['To'] = table['To'].str.upper()
table['From'] = table['From'].str.upper()
table.drop(columns=['To_From'], inplace=True)
table['Airline Code'] = table['Airline Code'].str.replace('[^A-Za-z\s]+', '', regex=True)
table = table.drop(table.tail(1).index)
print(table)
