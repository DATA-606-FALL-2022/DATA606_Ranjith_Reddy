# DATA606

# InstaCart - Online Grocery Analysis

![Instacart](https://digital.hbs.edu/platform-digit/wp-content/uploads/sites/2/2020/03/Instacart-Logo_0-1-1100x200.jpg)

## Description

Whether you shop from meticulously planned grocery lists or let whimsy guide your grazing, our distinct food rituals define who we are. Instacart, a grocery ordering and delivery app, aims to make it simple to stock your refrigerator and pantry with your personal favorites and staples when you need them. Personal shoppers review your order and do the in-store shopping and delivery for you after you select products via the Instacart application.


## Idea

- Huge demand and potential for online e-commerce. Companies have been leveraging data analysis to understand customer behavior, market trends, and machine learning for product recommendations. 
- In this project, I would like to analyze online grocery shopping data to gain insights about customer purchase and market trends. 
- I would like to use this anonymized data on customer orders over time to predict which previously purchased products will be in a user’s next order using classification techniques. 
- Further I would like to build a product recommender system that recommends products for a given user based on the available order history and similar user ratings using association rule mining. 


## About Data

Source: An online grocery shopping dataset is taken from Kaggle for the project.  This can be found at: 
https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset
Size of the dataset is 1.28 GB with around 3.4 Million user transactions recorded.
The dataset consists of 5 CSV files, each file describing a different aspect of the data including aisles, departments, orders, products and order behavior. Each entity (customer, product, order, aisle, etc.) has an associated unique id. Most of the files and variable names should be self-explanatory.
  1. aisles.csv(aisle id, aisle description)
  2. departments.csv(dept id, dept name)
  3. order_products.csv(order_id, product_id, add_to_cart_order, reordered)
  4. orders.csv(order_id, user_id, eval_set, order_number, order_dow, order_hour_of_delay, days_since_prior)
  5. products.csv(product_id, product_name, aisle_id, dept_id)



## Exploratory Data Analysis.

### we have following DataFrames:

   - orders: This table includes all orders, namely prior, train, and test. It has single primary key (order_id).
   - order_products_train: This table includes training orders. It has a composite primary key (order_id and product_id) and indicates whether a product        in an order is a reorder or not (through the reordered variable).
   - order_products_prior : This table includes prior orders. It has a composite primary key (order_id and product_id) and indicates whether a product in      an order is a reorder or not (through the reordered variable).
   - products: This table includes all products. It has a single primary key (product_id)
   - aisles: This table includes all aisles. It has a single primary key (aisle_id)
   - departments: This table includes all departments. It has a single primary key (department_id)

### Ratio of reordered products

  1. 58.9697% of products in prior orders were re-ordered.
  2. 59.8594% of products in train orders were re-ordered.
  3. 11.868056% of orders having no reordered product.
  4. 21.493998% of orders having all product re-ordered.
  5. Most baskets contain from 5-8 products.
  6. Products placed first in cart are the products mostly reordered.

### Analyzing the count of reordered products in a basket

  1. Most baskets have from 0-5 reordered product
  2. Probability of a basket having 0 reordered products: 11.868056
  3. Probability of a basket having 1 reordered products: 10.262626
  4. Probability of a basket having 2 reordered products: 10.326791
  5. Probability of a basket having 3 reordered products: 9.735981
  6. Probability of a basket having 4 reordered products: 8.777965

### Time effects on purchasing behaviours

  - How Time affects the purchasing behaviour of customers?
  - Most orders are ordered on Day 0 and Day 1.
  - Orders are mostly ordered during day, from 9:00 AM to 4:00 PM.
  - Peak orders happens at Saturday afternoon (1:00PM), and Sunday morning (10:00AM)
  - By more than 65%, People usually buy previously ordered products from 6:00AM to 8:00AM
  - Most users make orders after a week from their last order. or from a month of their last order.
  - After a week from the last order, the probability of reordering within the same month is small. 
      - Send reminders of the most likely ordered products within a week, to catch the high prob of a customer to make their next order.
  - The Next order has higher probability to be during 10 days from the current order.

### Association between days since last order and the ratio of reorders

  - 74 % of products bought at the same day of prev order, are reorders.
  - 69% of products bought after 1 week of prev order, are reorders
    #### Conculsion:
      - If future order will be at the same day of prev order, percentage of reorders in the future product is high.
      - If future order will be after a week from the prev order, percentage of reorders in the future product is high.


### Analyzing products

   #### How often a product is purchased?
   
   - 5 Most Ordered Products
        - Banana
        - Bag of Organic Bananas
        - Organic Strawberries
        - Organic Baby Spinach
        - Organic Hass Avocado
        - 14% of all orders contains bananas.  
   - Organic products are frequently ordered.

  #### How often a product is the first item purchased?
  
   - 5 Most Add to Cart First Products
        - Banana
        - Bag of Organic Bananas
        - Organic Whole Milk
        - Organic Strawberries
        - Organic Hass Avocado
   - 3.4% of the orders, Banana is being the first product added to cart. Products contianing milk have very high probability to be reordered. Organic          products have very high probability to be reordered.

### Analyzing Organic Prodcuts

   - 10% of instacart's products are organic products
   - 31.5% of bought products are organic products
   - 67% probability of reordering an organic products.
   - 61% probability of reordering an non-organic products.
   - No significance pattern of when organic products are bought most, than when products in general are bought most.

### Purchasing behaviour on Departments and Aisles

   - Count of products in each department
   - ![count of products](https://github.com/DATA-606-FALL-2022/DATA606_Ranjith_Reddy/blob/main/Images/Piechart.png)


## Modeling


### Logistic Regression

   - Based on the user_id we have predicted whether the user reordered the product or not.


   - ![logistic](https://github.com/DATA-606-FALL-2022/DATA606_Ranjith_Reddy/blob/main/Images/Logistic.png)


### K-means Clustering

   - Heatmap for share of purchases by aisle for the top 20 Instacart aisles.
   
   - ![kmeans](https://github.com/DATA-606-FALL-2022/DATA606_Ranjith_Reddy/blob/main/Images/Kmeans.png)


### Product Recomender

   - Deployment of this application is done using Streamlit which is an open-source Python library that makes it easy to create and share beautiful,            custom web apps for machine learning and data science.
   
   - ![pr](https://github.com/DATA-606-FALL-2022/DATA606_Ranjith_Reddy/blob/main/Images/product%20recomender.png)


## Conclusion
   - Instacart is a web app and in web analytics , data reflects the way users behave, and the way they are encouraged to behave, by the decisions earlier      made. Market Basket analysis can be used to drive business decision making by using the association results. There are number of ways in which MBA        can be used :
   - Associated Aisles should be placed together on the web application platform to boost the sales and reduce the time spent in finding that Aisle. For        instance, Cereal, lunch meat and Bread Aisle should be placed together, as they are highly associated.
   - Associated products such as Organic Cilantro and limes should be put close to one another, to improve the customer shopping experience and improving      the store layout. Marketing can take benefit from these association relationship, for example target customers who buy Organic Cilantro with offers        on Lime, to encourage them to spend more on their shopping basket.


## Future Scope

   - For predicting whether a product is reordered or not, algorithms that predict binomial categories better can be used.
   - For predicting a multi-category variable like department, other multi-nominal algorithms can be applied.
   - New features could be created to help us generalize better on the test dataset thereby achieving better results.
   
   
## Data 

- https://drive.google.com/drive/u/2/folders/1cYJDqAGylRg6JQgKjMZLqRSCdl6LHnFR

## Presentation

- https://github.com/DATA-606-FALL-2022/DATA606_Ranjith_Reddy/tree/main/Presentations


## References


- https://www.kaggle.com/code/nouranhany10/eda-on-instacart-data
- https://www.kaggle.com/c/instacart-market-basket-analysis/data?select=sample_submission.csv.zip 
- https://medium.com/mlearning-ai/instacart-market-basket-analysis-a726bb56d62



