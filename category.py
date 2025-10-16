# -*- coding: utf-8 -*-
# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Category class.

Step-by-step Instructions:
1. Create Category class with attributes:
   - category_id (int)
   - name (str)
   - products (list of Product objects)
2. Add methods:
   - add_product(product)
   - remove_product(product_id)
   - list_products() → return all products in this category
3. Ensure duplicate products are not added.

TODO for Students:
- Implement Category class.
- Link products properly.
- Use exceptions for invalid operations.
"""


# Handles product categories.
# TODO: Implement this file

# Category class groups products (e.g., Electronics, Clothing).
# It can track all products under that category.

class Category:
    def __init__(self, name):
        self.name=name
        self.category_id=0
        self.products={}
        

    def add_product(self, product):
        try:
           
            if product.product_id in self.products:
                raise Exception(f"Product with Product_id '{product.product_id}' already exists in Category '{self.name}'.")
                
            self.products[product.product_id]=product  
            
        except Exception as e:
            return f'Error : {e}'

    def remove_product(self, product_id):
        # TODO: Remove product by ID from category list
        try:
            removed_product = self.products.pop(product_id)
            return f" '{removed_product.name}' Product has been removed from the Category '{self.name}'."
        
        except Exception as e:
            return f'Error: {e}'
        
    def list_products(self):
        return self.products.values()

    def __str__(self):
        # TODO: String representation → Category name + product count
        product_count=len(self.products)
        return f"Category '{self.name}' has '{product_count}' Products."

