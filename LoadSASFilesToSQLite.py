#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Read SAS files using sas7bdat library and load them into DataFrames
sas_files = os.listdir(os.getcwd() + "/WWI/")
dataframes = {}

for folder in os.listdir(os.path.join(os.getcwd(), "WWI")):
    print("\n", folder)
    for file in os.listdir(os.path.join(os.getcwd(), "WWI", folder)):
        if file.endswith('.sas7bdat'):
            print(" ", file)
            df_name = os.path.splitext(file)[0]
            with SAS7BDAT(os.path.join(os.getcwd(), "WWI", folder, file)) as f:
                dataframes[df_name] = f.to_data_frame()
# Create a SQLite database connection and save DataFrames to the database
wwi = sqlite3.connect('wwi.db')
for name, df in dataframes.items():
    # Replace the table if it already exists
    df.to_sql(name, wwi, index = False, if_exists = 'replace')

