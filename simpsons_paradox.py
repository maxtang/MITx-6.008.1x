
# coding: utf-8

# In[1]:

from simpsons_paradox_data import *


# In[2]:

joint_prob_table[gender_mapping['female'], department_mapping['C'], admission_mapping['admitted']]


# In[3]:

joint_prob_table


# In[4]:

joint_prob_table.sum(axis=0)


# In[5]:

joint_prob_gender_admission = joint_prob_table.sum(axis=1)
joint_prob_gender_admission


# In[6]:

import pandas as pd
# pd.set_option('precision', 17)
# pd.set_eng_float_format(accuracy=5)


# In[7]:

department_mapping


# In[8]:

joint_prob_panel = pd.Panel(joint_prob_table, 
         items = gender_labels,
         major_axis = department_labels,
         minor_axis = admission_labels
        )
joint_prob_panel


# In[9]:

joint_prob_panel.sum(axis=0)


# In[10]:

get_ipython().magic('matplotlib inline')


# In[11]:

joint_prob_panel.sum(axis=0).plot()


# In[12]:

joint_prob_panel.sum(axis=1)


# In[13]:

joint_prob_panel.sum(axis=1).plot()


# In[14]:

joint_prob_panel.sum(axis=2)


# In[15]:

joint_prob_panel.sum(axis=2).plot()


# In[16]:

joint_prob_panel.sum(axis=1)['female'].loc['admitted']


# In[17]:

female_only = joint_prob_gender_admission[gender_mapping['female']]
female_only


# In[18]:

joint_prob_panel.sum(axis=1)['female']


# In[19]:

prob_admission_given_female = female_only / np.sum(female_only)
prob_admission_given_female


# In[20]:

joint_prob_panel.sum(axis=1)['female']/joint_prob_panel.sum(axis=1)['female'].sum()


# In[21]:

prob_admission_given_female_dict = dict(zip(admission_labels, prob_admission_given_female))
print(prob_admission_given_female_dict)


# In[22]:

joint_prob_panel.sum(axis=1)['male']/joint_prob_panel.sum(axis=1)['male'].sum()


# In[23]:

admitted_only = joint_prob_gender_admission[:, admission_mapping['admitted']]
admitted_only


# In[24]:

joint_prob_panel.sum(axis=1).loc['admitted']


# In[25]:

prob_gender_given_admitted = admitted_only / np.sum(admitted_only)
prob_gender_given_admitted_dict = dict(zip(gender_labels, prob_gender_given_admitted))
print(prob_gender_given_admitted_dict)


# In[26]:

joint_prob_panel.sum(axis=1).loc['admitted']/joint_prob_panel.sum(axis=1).loc['admitted'].sum()


# In[27]:

female_and_A_only = joint_prob_table[gender_mapping['female'], department_mapping['A']]
female_and_A_only


# In[28]:

joint_prob_table[gender_mapping['female'], department_mapping['B']]/joint_prob_table[gender_mapping['female'], department_mapping['B']].sum()


# In[29]:

joint_prob_panel


# In[30]:

joint_prob_panel['female'].loc['A']


# In[31]:

joint_prob_panel['male'].loc['D']['admitted']/joint_prob_panel['male'].loc['D'].sum()


# In[32]:

joint_prob_panel['female'].loc['B']/joint_prob_panel['female'].loc['B'].sum()


# In[33]:

joint_prob_panel['male']


# In[34]:

for d in department_labels:
    for g in gender_labels:
        print(g)
        print(joint_prob_panel[g].loc[d]/joint_prob_panel[g].loc[d].sum())
        print()

