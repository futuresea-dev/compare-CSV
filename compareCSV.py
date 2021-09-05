import pandas as pd


clever = pd.read_csv("clever.csv")
ad = pd.read_csv("ad.csv")

#fill zero string

clever = clever.drop_duplicates(subset='Staff_Id', keep="last")
clever['Staff_Id'] = clever['Staff_Id'].apply(lambda x: '{0:0>4}'.format(x))
ad['employeeID'] = ad['employeeID'].apply(lambda x: '{:.0f}'.format(x))
ad['employeeID'] = ad['employeeID'].apply(lambda x: '{0:0>4}'.format(x))


new_df = pd.merge(clever, ad[["employeeID", "description"]],  how='left', left_on=['Staff_Id'], right_on = ['employeeID'])

del new_df['employeeID']
new_df['Staff_Id'].apply(str)
new_df['Staff_Id'] = '="' + new_df['Staff_Id'] + '"'

new_df.to_csv("output.csv", sep=',', encoding='utf-8', index=False)

print("done")