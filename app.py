#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import streamlit as st


# In[9]:


cricket_data=pd.read_excel('C:\\Users\\abhij\\Desktop\\SANJAY\\Cricket\\2.World_Cup50\\2\\data.xlsx')
print(cricket_data.shape)
cricket_data.head()


# In[20]:


cricket_data.replace(to_replace='-',value=0,regex=True,inplace=True)


# In[21]:


# Convert columns to appropriate data types
cricket_data['Runs'] = cricket_data['Runs'].astype(int)
cricket_data['Bat Av'] = cricket_data['Bat Av'].astype(float)
cricket_data['100'] = cricket_data['100'].astype(int)
cricket_data['Wkts'] = cricket_data['Wkts'].astype(int)
cricket_data['Bowl Av'] = cricket_data['Bowl Av'].astype(float)
cricket_data['5'] = cricket_data['5'].astype(int)


# In[22]:


# Define the scoring system (you can adjust these values as per your preference)
points_per_run = 1
points_per_bat_av_above_40 = 5
points_per_century = 20
points_per_wkt = 10
points_per_bowl_av_below_25 = 5
points_per_five_wicket_haul = 25
points_per_catch = 5
points_per_stumping = 10


# In[23]:


# Function to calculate the score for each player
def calculate_player_score(row):
    batting_score = (row['Runs'] // 10) * points_per_run
    if row['Bat Av'] >= 40:
        batting_score += points_per_bat_av_above_40
    batting_score += row['100'] * points_per_century

    bowling_score = (row['Wkts'] // 5) * points_per_wkt
    if row['Bowl Av'] <= 25:
        bowling_score += points_per_bowl_av_below_25
    bowling_score += row['5'] * points_per_five_wicket_haul

    fielding_score = (row['Ct'] // 5) * points_per_catch
    fielding_score += row['St'] * points_per_stumping

    total_score = batting_score + bowling_score + fielding_score
    return total_score


# In[25]:


# Apply the scoring function to each row in the DataFrame
cricket_data['Score'] = cricket_data.apply(calculate_player_score, axis=1)


# In[26]:





# Streamlit app code
def main():
    st.title('Cricket Player Performance Analysis')

    st.header('Cricket Data')
    st.write(cricket_data)

    st.header('Top Performers')
    num_top_performers = st.slider('Select the number of top performers to display:', 1, len(cricket_data), 5)
    top_performers = cricket_data.nlargest(num_top_performers, 'Score')
    st.write(top_performers)

if __name__ == '__main__':
    main()


# In[ ]:




