import pandas as pd

url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"
target_table_name = "European Union Road Safety Facts and Figures"

# Fetch all tables on webpage that match 
# provided table name and return as list
df = pd.read_html(url, match=target_table_name)

# Grab the first table
df = df[0] if len(df) >= 1 else 'Table Not Found!'

# Drop unwanted columns
df.drop(
    ['Road Network Length (in km) in 2013[29]',
    'Number of People Killed per Billion km[30]',
    'Number of Seriously Injured in 2017/2018[30]'],
    axis=1,
    inplace=True
    )

# Rename columns to a cleaner version
df.rename(columns={
    'Area (thousands of km2)[24]'                           :'Area',
    'Population in 2018[25]'                                :'Population',
    'GDP per capita in 2018[26]'                            :'GDP per capita',
    'Population density (inhabitants per km2) in 2017[27]'  :'Population density',
    'Vehicle ownership (per thousand inhabitants) in 2016[28]':'Vehicle ownership',
    'Total Road Deaths in 2018[30]'                         :'Total road deaths',
    'Road deaths per Million Inhabitants in 2018[30]'       :'Road deaths per Million Inhabitants.',
    },
    inplace=True
)

# Add the year column with the default value of 2018 for all rows
df['Year'] = 2018


# Save to csv file in current directory
df.to_csv('european_union_road_safety_facts_and_figures.csv', index=False)

# Print the table to console
print(df)