# InstaCart - Online Grocery Analysis
![Instacart](https://digital.hbs.edu/platform-digit/wp-content/uploads/sites/2/2020/03/Instacart-Logo_0-1-1100x200.jpg)

## Description

Whether you shop from meticulously planned grocery lists or let whimsy guide your grazing, our distinct food rituals define who we are. Instacart, a grocery ordering and delivery app, aims to make it simple to stock your refrigerator and pantry with your personal favorites and staples when you need them. Personal shoppers review your order and do the in-store shopping and delivery for you after you select products via the Instacart application.


## Idea

- Huge demand and potential for online e-commerce. Companies have been leveraging data analysis to understand customer behavior, market trends, and machine learning for product recommendations. 
- In this project, I would like to analyze online grocery shopping data to gain insights about customer purchase and market trends. 
- I would like to use this anonymized data on customer orders over time to predict which previously purchased products will be in a user’s next order. 
- Further I would like to build a product recommender system that recommends products for a given user based on the available order history and similar user ratings. 


## About Data

Source: An online grocery shopping dataset is taken from Kaggle for the project.  This can be found at: 
https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset
Size of the dataset is 1.28 GB with around 3.4 Million user transactions recorded.
The dataset consists of 5 CSV files, each file describing a different aspect of the data including aisles, departments, orders, products and order behavior.
  1. aisles.csv(aisle id, aisle description)
  2. departments.csv(dept id, dept name)
  3. order_products.csv(order_id, product_id, add_to_cart_order, reordered)
  4. orders.csv(order_id, user_id, eval_set, order_number, order_dow, order_hour_of_delay, days_since_prior)
  5. products.csv(product_id, product_name, aisle_id, dept_id)
  
  
## To do list

  - Which day of the week most orders are placed?
  - Which hour of the day most orders are placed?
  - Which aisles are most busy?
  - Which aisles are most busy in a given hour of the day?
  - How often do people place grocery orders?
  - Which department is most busy?
  - Which departments are most busy in a given hour of the day?
  - Which products have the most demand?
  - Which products were added first to the cart majority times?
  - Which hour of the day are each of the departments most busy?

## Unit of analysis for project will be Instacart users

## Variables and Measures

I would like to use these variables and measures:
  - user_id, 
  - department_name, 
  - reordered, 
  - order_hour_of_day, 
  - days_since_prior_order, 
  - add_to_cart_order, 
  - aisle_name

## Techniques and Models

To predict whether or not the user will reorder the item using classification algorithms such as:
  - Random forest
  - Support vector machine
  - Decision tree
  - K-nearest neighbor
  - Logistic Regression



## The project's flow

After Exploratory Data Analysis, I would like to build a model using a pipeline which involves  pre-processing, feature selection, classification and post-processing. For optimization I would like to use hyper-parameter tuning to tune the model. To determine the accuracy of all the classifiers, a voting classifier and Boosting techniques will be used. 


## Outcomes

I intend to create a Web application using Django or Flask. This project has two modules:
  - To predict whether or not the user will reorder the item using above classification algorithms. 
  - To get top 10 product recommendations based on previous purchases for a user.







