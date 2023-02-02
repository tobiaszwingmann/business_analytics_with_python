import pandas as pd

def flag_wholesale(quantity):
  quantity_avg = 12.3
  quantity_std = 39.36

  if quantity >= (quantity_avg + 3 * quantity_std):
    return "B2B"
  else:
    return "B2C"

df = pd.read_excel("retail_data_s.xlsx", sheet_name = "Data")
df_clean = df.query("StockCode != 'M'")
df_clean = df_clean.query("UnitPrice > 0")
df_clean['Revenue'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['Segment'] = df_clean['Quantity'].map(flag_wholesale)

print(pd.pivot_table(df_clean, index = ['Segment'], values = ['Revenue'], aggfunc = ['sum']))

(pd
.pivot_table(df_clean, index = ['Segment'], values = ['Revenue'], aggfunc = 'sum' )
.plot
.bar()
.get_figure()
.savefig('barchart.png'))