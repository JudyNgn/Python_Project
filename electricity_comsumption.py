## Daily and monthly electricity consumption (kWh) ##
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../electricity_data.csv')
df
data = pd.read_csv('../electricity_data.csv')

data['DateTime'] = pd.to_datetime(data['DateTime'])


daily_consumption = data.groupby(pd.Grouper(key="DateTime", freq="1d"))['Consumption'].sum()
monthly_consumption = data.groupby(pd.Grouper(key="DateTime", freq="1M"))['Consumption'].sum()

 # Visualize daily consumption
plt.figure(figsize=(12, 6))
daily_consumption.plot(title='Daily Electricity Consumption (kWh)')
plt.xlabel('Date')
plt.ylabel('Consumption (kWh)')
plt.show()

 # Visualize monthly consumption
plt.figure(figsize=(12, 6))
monthly_consumption.plot(kind='bar', title='Monthly Electricity Consumption (kWh)')
plt.xlabel('Date')
plt.ylabel('Consumption (kWh)')
plt.show()

## Daily and Monthly Average Electricity Price (c/kWh) ##
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../electricity_data.csv')
df
data = pd.read_csv('../electricity_data.csv')
#Daily and monthly electricity consumption (kWh)
data['DateTime'] = pd.to_datetime(data['DateTime'])
# Calculate daily average price
daily_avg_price = data.groupby(pd.Grouper(key="DateTime", freq="1d"))['Price'].mean()


monthly_avg_price = data.groupby(pd.Grouper(key="DateTime", freq="1M"))['Price'].mean()

 # Visualize daily average price
plt.figure(figsize=(12, 6))
daily_avg_price.plot(title='Daily Average Electricity Price (c/kWh)')
plt.xlabel('Date')
plt.ylabel('Price (c/kWh)')
plt.show()

 # Visualize monthly average price
plt.figure(figsize=(12, 6))
monthly_avg_price.plot(kind='bar', title='Monthly Average Electricity Price (c/kWh)')
plt.xlabel('Date')
plt.ylabel('Price (c/kWh)')
plt.show()

## Calculate Daily and Monthly Electricity Bills for Different Fixed Price Scenarios (5c/kWh, 10c/kWh, 20c/kWh)##
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../electricity_data.csv')
df
data = pd.read_csv('../electricity_data.csv')
#Daily and monthly electricity consumption (kWh)
data['DateTime'] = pd.to_datetime(data['DateTime'])
fixed_prices = [5, 10, 20]  # Fixed price scenarios in cents per kWh

 # Calculate daily and monthly bills for each fixed price scenario 
for price in fixed_prices:
    data['Bill_' + str(price)] = data['Consumption'] * (price / 100)  # Price is in cents

 # Calculate daily and monthly total bills for each fixed price scenario

daily_total_bills = data.groupby(pd.Grouper(key="DateTime", freq="1d"))[[f'Bill_{price}' for price in fixed_prices]].sum()
monthly_total_bills = data.groupby(pd.Grouper(key="DateTime", freq="1M"))[[f'Bill_{price}' for price in fixed_prices]].sum()

 # Visualize daily total bills for different fixed price scenarios
plt.figure(figsize=(12, 6))
daily_total_bills.plot(title='Daily Total Electricity Bills for Different Fixed Prices (€)')
plt.xlabel('Date')
plt.ylabel('Total Bill (€)')
plt.legend([f'{price}c/kWh' for price in fixed_prices])
plt.show()

 # Visualize monthly total bills for different fixed price scenarios
plt.figure(figsize=(15, 20))
monthly_total_bills.plot(kind='bar', title='Monthly Total Electricity Bills for Different Fixed Prices (€)')
plt.xlabel('Date')
plt.ylabel('Total Bill (€)')
plt.legend([f'{price}c/kWh' for price in fixed_prices])
plt.show()

 #Relation between Outside Temperature, Consumption, and Total Bill
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../electricity_data.csv')
df
data = pd.read_csv('../electricity_data.csv')
#Daily and monthly electricity consumption (kWh)
data['DateTime'] = pd.to_datetime(data['DateTime'])
# Calculate daily average temperature
daily_avg_temperature = data.groupby(pd.Grouper(key="DateTime", freq="1d"))['Temperature'].mean()

 # Visualize the relationship between temperature and consumption
plt.figure(figsize=(12, 6))
plt.scatter(daily_avg_temperature, daily_consumption, alpha=0.5)
plt.title('Daily Consumption vs. Average Daily Temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Consumption (kWh)')
plt.show()

 # Visualize the relationship between temperature and total bill for different fixed price scenarios
plt.figure(figsize=(12, 6))
for price in fixed_prices:
    plt.scatter(daily_avg_temperature, daily_total_bills[f'Bill_{price}'], alpha=0.5, label=f'{price}c/kWh')
plt.title('Daily Total Bill vs. Average Daily Temperature for Different Fixed Prices (€)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Total Bill (€)')
plt.legend()
plt.show()

## Relation between Outside Temperature, Consumption, and Total Bill ##
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../electricity_data.csv')
df
data = pd.read_csv('../electricity_data.csv')
#Daily and monthly electricity consumption (kWh)
data['DateTime'] = pd.to_datetime(data['DateTime'])
# Calculate daily average temperature
daily_avg_temperature = data.groupby(pd.Grouper(key="DateTime", freq="1d"))['Temperature'].mean()

 # Visualize the relationship between temperature and consumption
plt.figure(figsize=(12, 6))
plt.scatter(daily_avg_temperature, daily_consumption, alpha=0.5)
plt.title('Daily Consumption vs. Average Daily Temperature')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Consumption (kWh)')
plt.show()

 # Visualize the relationship between temperature and total bill for different fixed price scenarios
plt.figure(figsize=(12, 6))
for price in fixed_prices:
    plt.scatter(daily_avg_temperature, daily_total_bills[f'Bill_{price}'], alpha=0.5, label=f'{price}c/kWh')
plt.title('Daily Total Bill vs. Average Daily Temperature for Different Fixed Prices (€)')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Total Bill (€)')
plt.legend()
plt.show()

Critical Factors in Electricity Consumption and Total Bill:

- Consumption:

Seasonal Variations: Colder weather increases heating demands, while hot weather raises cooling needs.
Daily Patterns: Routines, occupancy, and peak-hour reductions affect daily consumption.
Energy Efficiency: Efficient practices and appliances help reduce overall consumption.

- Total Bill:

Contract Choice: Variable-rate and fixed-rate contracts impact the bill. Fixed rates provide predictability, while variable rates lead to fluctuations.
Seasonal Prices: Supply and demand fluctuations cause seasonal price variations.
Temperature & Weather: Cold weather increases consumption, and extreme conditions can lead to price spikes.
Energy Efficiency: Lower consumption and efficient technologies result in cost savings.

