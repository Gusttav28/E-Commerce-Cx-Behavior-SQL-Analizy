# E-Commerce-Cx-Behavior-SQL-Analizy

This is a repository in where I going to analizy the e commerce customers behavior data set with just Sql, than I going to share the results of the analize and I'm going to develop full stack software in where I can show this results

So I'm going to devide each type of job analize from the most "basic" to the most advance.
In this case the main objective is to tried to simulate a "real data analizys work" in where I need to write queries to each specific case.

# Beginner (Filtering and Basic Analysis):

[x]Find all orders where the payment method is “Credit Card.”

query: SELECT product_category, payment_method, Count(payment_method) FROM `e-commerce-behavior`.`e-commerce-behavior` where payment_method = 'Credit Card' group by product_category;

query explanation: The result of this query shouold show us a filter in where we can find all the product category that have been pay by a credit card and also the amount of times that this product category have been pay with a credit card. Example: product category: electronics, payment method: credit card, amount of payments time: 322.

[x]Show orders with a value greater than $500.

query 1: SELECT product_category, order_value_usd FROM `e-commerce-behavior`.`e-commerce-behavior` where order_value_usd > 500;
query 1 explanation: This query is showing us the product categories that are more grather than $500

query 2: SELECT product_category, count(order_value_usd) FROM `e-commerce-behavior`.`e-commerce-behavior` where order_value_usd > 500 group by product_category;
query 2 explanation: This other queary is showing us the amount of products categories that are grather than %500 by group. Example: We have the sports category product that has 1130 order values grather than %500

[x]Count how many orders were returned vs not returned.

query 1: SELECT returned, count(order_value_usd) as "orders_returned" FROM `e-commerce-behavior`.`e-commerce-behavior` where returned = 'No' or returned = 'Yes' group by returned;
query 1 explanation: This query is showing us the amount of orders that have been returned and the one have not being returned.

[x]List all orders made after a specific date.
query: SELECT product_category, order_value_usd, order_date FROM `e-commerce-behavior`.`e-commerce-behavior` where order_date > '2023-11-24';
query explanationte: This query is showing us all the orders made after 2023-11-24 that was a black friday and also which products category are the ones that have been in those orders.

[x]Get the average order value for all orders.
query: SELECT avg(order_value_usd) as "AVG_Orders" FROM `e-commerce-behavior`.`e-commerce-behavior`;
query explanation: This query is showing us a row with the expected result.
