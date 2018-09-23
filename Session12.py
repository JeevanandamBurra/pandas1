
# coding: utf-8

# In[1]:


import pandas as pd
from pandas import DataFrame, Series
import sqlite3 as db
from pandasql import sqldf


# In[2]:


df=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',sep=',',header=None)


# In[3]:


Dff=df.head(100)


# In[4]:


Dff.columns = ['age', 'workclass','fnlwgt','education','educationnum','maritalstatus','occupation','relationship',
               'race','sex','capitalgain','capitalloss','hoursperweek','nativecountry','label']


# In[5]:


Dff.head()


# In[9]:


#create_connection("C:\\sqlite\db\sqldb.db")
conn = db.connect('sqldb.db')


# In[10]:


c = conn.cursor()


# In[11]:


c.execute(''' CREATE TABLE IF NOT EXISTS adlt ( age int, workclass TEXT, fnlwgt int, education TEXT, educationnum int, 
                maritalstatus TEXT, occupation TEXT,
                relationship TEXT, race TEXT,sex TEXT,capitalgain int,capitalloss int,
                hoursperweek int,nativecountry TEXT,label TEXT);''')


# In[12]:


Dff.to_sql('adlt',conn, if_exists='append', index = False)


# ## 1. Select 10 records from the adult sqladb

# In[15]:


q=""" select * from adlt limit 5 """


# In[16]:


pd.read_sql_query(q,conn)


# ## 2. Show me the average hours per week of all men who are working in private sector

# In[17]:


c.execute("select avg(hoursperweek) from adlt where sex=:sex and workclass=:wk", {"sex":'Male',"wk":'Private'})

c.fetchall()


# In[18]:


q=""" select avg(hoursperweek) from adlt where sex='Male' and workclass='Private' """


# In[19]:


pd.read_sql_query(q,conn)


# ## 3. Show me the frequency table for education, occupation and relationship, separately

# In[22]:


ed="Select education, count(*) From   adlt Group By education"

c.execute(ed).fetchall()


# In[24]:



occ="Select occupation, count(*) From   adlt Group By occupation"

c.execute(occ).fetchall()


# In[26]:


rel="Select relationship, count(*) From   adlt Group By relationship"

c.execute(rel).fetchall()


# ## 4. Are there any people who are married, working in private sector and having a masters degree

# In[30]:


md=c.execute("select * from adlt where education='Masters' and workclass='Private' and relationship in ('Husband','Wife')")

for row in md:

    print(row)


# In[ ]:


q="""select * from adlt where education='Masters' and workclass='Private' and relationship in ('Husband','Wife'); """
pd.read_sql_query(q,conn)


# ## 5. What is the average, minimum and maximum age group for people working in
# different sectors

# In[33]:


q="""Select workclass,avg(age),min(age),max(age) From  adlt Group By workclass """

pd.read_sql_query(q,conn)


# ## 6. Calculate age distribution by country

# In[36]:


q="""select avg(age),nativecountry from adlt group by nativecountry """
pd.read_sql_query(q,conn)


# ## 7 add new

# In[42]:


q=""" select * from adlt limit 5 """
pd.read_sql_query(q,conn)


# In[ ]:


q=""" ALTER TABLE adlt ADD COLUMN 'Net_Capita_lGain' int; """
pd.read_sql_query(q,conn)


# In[ ]:


q="""UPDATE adlt SET Net_Capita_lGain == (capitalgain - capitalloss) """
pd.read_sql_query(q,conn)


# In[47]:


q=""" select * from adlt limit 15 """
pd.read_sql_query(q,conn)

