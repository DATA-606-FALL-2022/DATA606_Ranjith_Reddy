#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from itertools import combinations, groupby, chain
from collections import Counter


# In[2]:


cluster0_item_rules = pd.read_csv('data/group0_item_rules.csv', index_col = 0)
cluster1_item_rules = pd.read_csv('data/group1_item_rules.csv', index_col = 0)
cluster2_item_rules = pd.read_csv('data/group2_item_rules.csv', index_col = 0)
cluster3_item_rules = pd.read_csv('data/group3_item_rules.csv', index_col = 0)
cluster4_item_rules = pd.read_csv('data/group4_item_rules.csv', index_col = 0)
cluster5_item_rules = pd.read_csv('data/group5_item_rules.csv', index_col = 0)
cluster0_aisle_rules = pd.read_csv('data/group0_aisle_rules.csv', index_col = 0)
cluster1_aisle_rules = pd.read_csv('data/group1_aisle_rules.csv', index_col = 0)
cluster2_aisle_rules = pd.read_csv('data/group2_aisle_rules.csv', index_col = 0)
cluster3_aisle_rules = pd.read_csv('data/group3_aisle_rules.csv', index_col = 0)
cluster4_aisle_rules = pd.read_csv('data/group4_aisle_rules.csv', index_col = 0)
cluster5_aisle_rules = pd.read_csv('data/group5_aisle_rules.csv', index_col = 0)


# In[3]:


products = pd.read_csv('data/products.csv', index_col = 0)
aisles = pd.read_csv('data/aisles.csv', index_col = 0)
clusters = pd.read_csv('data/cluster_df.csv', index_col = 0)


# In[4]:


cluster_df = clusters.set_index('user_id')
cluster_df


# In[5]:


cluster_item_rules_dic = {}
cluster_item_rules_dic[0] = cluster0_item_rules
cluster_item_rules_dic[1] = cluster1_item_rules
cluster_item_rules_dic[2] = cluster2_item_rules
cluster_item_rules_dic[3] = cluster3_item_rules
cluster_item_rules_dic[4] = cluster4_item_rules
cluster_item_rules_dic[5] = cluster5_item_rules


# In[6]:


cluster_item_rules_dic[4]


# In[7]:


cluster_aisle_rules_dic = {}
cluster_aisle_rules_dic[0] = cluster0_aisle_rules
cluster_aisle_rules_dic[1] = cluster1_aisle_rules
cluster_aisle_rules_dic[2] = cluster2_aisle_rules
cluster_aisle_rules_dic[3] = cluster3_aisle_rules
cluster_aisle_rules_dic[4] = cluster4_aisle_rules
cluster_aisle_rules_dic[5] = cluster5_aisle_rules


# In[8]:


cluster_aisle_rules_dic[4]


# In[9]:


# returns top x items associated based on lift

def product(cluster, product_id, item_lift, product_name, num_products):
    df = cluster_item_rules_dic[cluster]
    df = df[(df['item_A'] == product_id) | (df['item_B'] == product_id)][['product_name_A','item_A','product_name_B','item_B','confidenceAtoB','lift']].sort_values('lift', ascending = False)
    df = df[df['lift'] > item_lift]
    df = df.sort_values('lift', ascending = False)
    df = df.head(n = num_products)
    product_associations = df['product_name_A'].values.tolist()
    for x in df['product_name_B'].values.tolist():
        product_associations.append(x)
    product_associations = [x for x in product_associations if x != product_name]
    return product_associations


# In[17]:


# returns recommended products given inputs

def prod_recommender(user_id, product_id, item_lift, num_products):
    product__id = 39055
    item__lift = 1
    product_name = products.at[product_id,'product_name']
    aisle_id = products.at[product_id,'aisle_id']
    aisle_name = aisles.at[aisle_id,'aisle']
    cluster = cluster_df.at[user_id, 'cluster']
    print(cluster)
    return product(cluster = cluster, product_id = product_id, item_lift = item_lift, 
                              product_name = product_name, num_products = num_products)


# In[18]:


user__id = int(input("Enter user id "))
product__id = 39055
item__lift = 1
num__products = int(input("Enter Number of recommendations "))


# In[19]:


prod_recommender(user__id,product__id,item__lift,num__products)


# In[13]:


import pickle
ser=pickle.dumps(prod_recommender)


# In[15]:


id2 = pickle.loads(ser)
id2(100,39055,1,5)


# In[24]:


pickle.dump(prod_recommender, open('model1.pkl','wb'))


# In[22]:


model1 = pickle.load(open('model1.pkl', 'rb'))


# In[23]:


model1


# In[ ]:




