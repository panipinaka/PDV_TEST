#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Using the dataset “milk_production.csv”, write script and create the visualizations.


# In[154]:


import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


data=pd.read_csv("milk_production.csv")


# In[5]:


data


# In[7]:


df=data.fillna(0)  #filling nan value with zero 


# In[133]:


#1.Which state has produced max milk in year 2013-14?

df["total_13-14"]=df["Cow Milk-2013-14"]+df["Boffalo Milk-2013-14"]+df["Goat Milk-2013-14"]
df[df["total_13-14"]==df["total_13-14"].max()]["State/ UT Name"]


# In[142]:


#2.List top 5 milk producing states in each year from 2010 to 2015

df["year_10"]=df["Cow Milk-2010-11"]+df["Boffalo Milk-2010-11"]+df["Goat Milk-2010-11"]
df["year_11"]=df["Cow Milk-2011-12"]+df["Boffalo Milk-2011-12"]+df["Goat Milk-2011-12"]
df["year_13"]=df["Cow Milk-2013-14"]+df["Boffalo Milk-2013-14"]+df["Goat Milk-2013-14"]
df["year_14"]=df["Cow Milk-2014-15"]+df["Boffalo Milk-2014-15"]+df["Goat Milk-2014-15"]
df["year_15"]=df["Cow Milk-2015-16"]+df["Boffalo Milk-2015-16"]+df["Goat Milk-2015-16"]

print("year 10")
print(df.sort_values(['year_10'],ascending=False)["State/ UT Name"].head())##year 10
print("year 11")
print(df.sort_values(['year_11'],ascending=False)["State/ UT Name"].head())#year 11
print("year 13")
print(df.sort_values(['year_13'],ascending=False)["State/ UT Name"].head())#year 13
print("year 14")
print(df.sort_values(['year_14'],ascending=False)["State/ UT Name"].head())#year 14
print("year 15")
print(df.sort_values(['year_15'],ascending=False)["State/ UT Name"].head())#year 15


# In[152]:


#3.Calculate average milk production by cow, buffalo and goat in each year for selected state.
df["total_cow"]=df["Cow Milk-2010-11"]+df["Cow Milk-2011-12"]+df["Cow Milk-2013-14"]+df["Cow Milk-2014-15"]+df["Cow Milk-2015-16"]
df[df["total_cow"].mean() and df["State/ UT Name"]=="Uttar Pradesh"]


# In[151]:


#3.Calculate average milk production by cow, buffalo and goat in each year for selected state.
df["total_boffolo"]=df["Boffalo Milk-2010-11"]+df["Boffalo Milk-2011-12"]+df["Boffalo Milk-2013-14"]+df["Boffalo Milk-2014-15"]+df["Boffalo Milk-2015-16"]
df[df["total_boffolo"].mean() and df1["State/ UT Name"]=="Assam"]


# In[150]:


#3.Calculate average milk production by cow, buffalo and goat in each year for selected state.
df["total_goat"]=df["Goat Milk-2010-11"]+df["Goat Milk-2011-12"]+df["Goat Milk-2013-14"]+df["Goat Milk-2014-15"]+df["Goat Milk-2015-16"]
df[df["total_goat"].mean() and df["State/ UT Name"]=="Chhattisgarh"]


# In[159]:


#4.List 5 states (if present) whose total milk production is increased for last three years.
df[df["year_14"].ge(df["year_14"]) & df["year_14"].ge(df["year_13"])].head()


# In[162]:


#Draw line graph showing total milk production for last 5 years of selected state

x = ["year_10","year_11","year_13","year_14","year_15"]
y = [df.get_value(26,"year_10"),df.get_value(26,"year_11"),df.get_value(26,"year_13"),df.get_value(26,"year_14"),df.get_value(26,"year_15")]
plt.plot(x,y,label="milk production of up",marker="o")
plt.xlabel("last 5years")
plt.ylabel("milk production in ltrs")
plt.legend()
plt.show()


# In[178]:


#Draw subplots of pie charts showing % milk productions by cow, buffalo and goat for last 4 years of selected state.

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

colors = ['yellow', 'blue','green',"orange"]
labels = ["2010-11","2013-14","2014-15","2015-16"]
cow =[df.get_value(0,"Cow Milk-2011-12"),df.get_value(0,"Cow Milk-2013-14"),df.get_value(0,"Cow Milk-2014-15"),df.get_value(0,"Cow Milk-2015-16")]
boffalo =[df.get_value(0,"Boffalo Milk-2011-12"),df.get_value(0,"Boffalo Milk-2013-14"),df.get_value(0,"Boffalo Milk-2014-15"),df.get_value(0,"Boffalo Milk-2015-16")]
goat =[df.get_value(0,"Goat Milk-2011-12"),df.get_value(0,"Goat Milk-2013-14"),df.get_value(0,"Goat Milk-2014-15"),df.get_value(0,"Goat Milk-2015-16")]
ax1.set_title("cow_milk production")
ax2.set_title("Boffalo_milk production")
ax3.set_title("goat_milk production")
ax1.pie(cow,labels=labels,colors=colors, shadow=True, startangle=90,autopct='%1.1f%%')
ax2.pie(boffalo,labels=labels, colors=colors, shadow=True, startangle=90,autopct='%1.1f%%')
ax3.pie(goat, labels=labels,colors=colors, shadow=True, startangle=90,autopct='%1.1f%%')

plt.axis('equal')

plt.show()


# In[165]:





# In[ ]:




