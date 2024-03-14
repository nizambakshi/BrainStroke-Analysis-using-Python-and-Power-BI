#!/usr/bin/env python
# coding: utf-8

# # first import the library

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')


# # import the data set

# In[6]:


df = pd.read_csv(r'C:\Users\Nizam Bakshi\Downloads\Filtered_data.csv')


# # Exploratory Data Analysis and Data Cleaning

# # we can only do the eda on the general data not the personal data like name, mobile no.  etc........

# In[7]:


df


# In[8]:


df.shape


# # as there are 4158 rows in the data and 11 columns

# In[9]:


df.columns


# In[10]:


df.head()


# In[11]:


df.tail()


# # To check the data type

# In[12]:


df.info()


# # we need to check the object type column values

# In[13]:


df.describe(include = 'object')


# here the machine has taken the object data

# # to check the statistical values for the numerical data

# In[14]:


df.describe()


#  here the machine has taken the numerical data to show

# # Now lets see for the object data type

# In[15]:


for col in df.describe(include = 'object').columns :
    print(col)
    print(df[col].unique())
    print('-'*50)


# As from above we get the values that are present in the object column

# # Now we have to check whether there are missing values

# In[16]:


df.isnull().sum()


# as all  are 0 then there is no missing values in the data

# In[17]:


df['age'].plot(kind ='box')


# as from here you get to know that the quartile the data of particular column

# In[16]:


df.describe()


# As there no outliers in the data so we can proceed further
# outliers are those extreme values of the data it can from -1 to 100000
# so to make the data ready for the analysis we need to clean and filter and remove the outliers if needed
# # so Analyse the clean data

# # Data Analysis and Visualization

# first we will check the percentage of the brain stroke happened to the patient

# In[17]:


brain_stroke = df['stroke'].value_counts(normalize = True)
print(brain_stroke)


# In[18]:


brain_stroke


# # So lets visualize the above data

# In[19]:


plt.figure(figsize = (5,5))
plt.title('Stroke among the patients')
plt.bar(['Not Stroked','Stroked'],df['stroke'].value_counts(), width = 0.5)
plt.show()
print(brain_stroke)


# As you can see that the 95% of the patient doesn't have stroke while 6% have stroke

# # As you can seen that this is a minor issue in the patient as the majority of the patient doesnt have stroke

# In[21]:


plt.figure(figsize = (8,4))
ax1 = sns.countplot(x = 'gender', hue = 'stroke', data = df, palette = 'Blues')
legend_lables,_=ax1. get_legend_handles_labels()
plt.title('Stroke Status in Male and Female',size = 20)
plt.xlable('Gender')
plt.ylabel('No. of Stroke')
plt.legend(['Not Stroked','Stroked'])
plt.show()


# from the above graph

# female gender has the most stroke as well as no stroke

# while male has less as compared to female

# In[66]:


female = df[df['gender']=='Female']
female['stroke'].value_counts(normalize = True)


# In[67]:


male = df[df['gender']=='Male']
male['stroke'].value_counts(normalize = True)


# In[68]:


male = df[df['gender']=='Male']
male['hypertension'].value_counts(normalize = True)


# In[69]:


female = df[df['gender']=='Female']
female['hypertension'].value_counts(normalize = True)


# In[70]:


male = df[df['gender']=='Male']
male['heart_disease'].value_counts(normalize = True)


# In[71]:


female = df[df['gender']=='Female']
female['heart_disease'].value_counts(normalize = True)


# from above we get that male population is having more problems then female population
# 

# In[37]:


female = female.groupby('age')[['bmi']].mean()
male = male.groupby('age')[['bmi']].mean()


# In[41]:


plt.figure(figsize = (20,10))
plt.title('Average Bmi of Male and female', fontsize = 20)
plt.plot(female.index,female['bmi'], label = 'female')
plt.plot(male.index,male['bmi'], label = 'male')
plt.legend(fontsize = 20)
plt.xlabel('Age')
plt.ylabel('Bmi')
plt.show()


# as from above graph as you can see that from 15 age the bmi takes a boost and the average bmi from age 20 to 80 is from 25 to 32

# In[42]:


df.head()


# In[43]:


['avg_glucose_level']


# In[72]:


female = female.groupby('age')[df['avg_glucose_level']].mean()
male = male.groupby('age')[df['avg_glucose_level']].mean()


# In[73]:


df.corr()


# In[ ]:




