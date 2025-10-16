# -*- coding: utf-8 -*-

# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Store class.

Step-by-step Instructions:
1. Create Store class with attributes:
   - name (str)
   - products (dict → product_id: Product)
   - categories (dict → category_id: Category)
2. Methods:
   - add_product(product)
   - remove_product(product_id)
   - update_stock(product_id, qty)
   - get_product(product_id) → return Product object
   - list_all_products()
3. Ensure error handling:
   - Invalid product IDs
   - Negative stock updates

TODO for Students:
- Implement Store class methods.
- Maintain consistent product and category mappings.
- Use custom exceptions for errors.
"""


# Handles the Store class and product operations.
# TODO: Implement this file
# Store class manages all products and categories.
# Acts like a central manager.

from product import Product
from category import Category
from exceptions import ProductNotFoundError, InvalidOperationError

class Store:
    def __init__(self,name):
        self.name=name
        self.products={}
        self.categories={}
        

    def add_product(self, product):
        if not isinstance(product, Product):
            raise InvalidOperationError("Only Product instances can be added.")
            
        self.products[product.product_id]= product
        print(f"Product '{product.name}' added  in the Product List. ")
        
        # rest for category
        category_name=product.category
        if category_name not in self.categories:
            self.categories[category_name]=[]
        self.categories[category_name].append(product)

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
           
            
        removed_product=self.products.pop(product_id)
        print( f" Product '{removed_product.name}' has been removed from the List.")
        
        # rest of category
        category_name=removed_product.category
        if category_name in self.categories:
            self.categories[category_name]=[p for p in self.categories[category_name] if p.product_id !=product_id]
            
            if not self.categories[category_name]:
                self.categories.pop(category_name)
        print(f"Product with ID '{product_id}' has been removed from the category.")

    def update_stock(self, product_id, qty):
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        
        result=self.products[product_id].update_stock(qty)
        print(f'Quantity of the product is updated {qty}')
        return result

    def update_price(self, product_id, new_price):
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        
        result=self.products[product_id].update_price(new_price)
        print(f'Price of the product is updated {new_price}')
        return result

    def apply_discount_to_category(self, category_name, percent):
        if category_name not in self.categories:
            raise ProductNotFoundError("Category not Found !")
            
        if percent <=0 or percent>100:
            raise InvalidOperationError(f" '{percent}' not valid !")
            
        
        for discount in self.categories[category_name]:
            discount.apply_discount(percent)  
        

    def list_all_products(self):
        return list(self.products.values())

    def find_product(self, product_id):
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product ID {product_id} not found.")
        
        return self.products[product_id]    

