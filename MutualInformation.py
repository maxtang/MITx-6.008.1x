
# coding: utf-8
Part 1: Probability and Inference > Week 4: Measuring Randomness > Exercise: Mutual Information
https://courses.edx.org/courses/course-v1:MITx+6.008.1x+3T2016/courseware/1__Probability_and_Inference/info_measures/
# In[1]:

import numpy as np
joint_prob_XY = np.array([[0.10, 0.09, 0.11], [0.08, 0.07, 0.07], [0.18, 0.13, 0.17]])
joint_prob_XY


# In[2]:

prob_X = joint_prob_XY.sum(axis=1)
prob_X


# In[3]:

prob_Y = joint_prob_XY.sum(axis=0)
prob_Y


# In[4]:

joint_prob_XY_indep = np.outer(prob_X, prob_Y)
joint_prob_XY_indep


# In[ ]:



