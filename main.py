# -*- coding: utf-8 -*-

# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Main entry point of the Inventory Management System.

Step-by-step Instructions:
1. Import classes: Product, Category, Store, Report.
2. Create a Store object (this will hold all products and categories).
3. Implement a simple menu system:
   a. Add product
   b. Remove product
   c. Update stock
   d. Generate report
   e. Exit
4. Use input() to interact with the user.
5. Call appropriate Store methods based on the menu choice.

TODO for Students:
- Implement the menu logic.
- Make sure invalid choices are handled using try/except.
- Provide clean output for the user.
"""
# TODO: Import required classes here
# from product import Product
# from store import Store
# from report import Report


# Entry point for the system.
# TODO: Implement this file

# Entry point (menu-driven interface).
# Students will implement CLI to test functionality.

from store import Store
from product import Product
from report import Report


def main():
    # TODO: Create Store instance
    # TODO: Add some sample products
    # TODO: Menu options:
    #   1. Add Product
    #   2. Remove Product
    #   3. Update Stock
    #   4. Update Price
    #   5. Apply Discount
    #   6. Show Reports
    #   7. Export Data
    store=Store('Sam Global Store')
    prod1 = Product(11, 'Laptop', 70000, 5, 'Electronics')
    prod2 = Product(12, 'Shirt', 1500, 10, 'Fashion')
    prod3 = Product(13, 'Iphone', 90000, 3, 'Electronics')
    for prod in [prod1,prod2, prod3]:
        store.add_product(prod)

    while True:
        print('1. Add Product')
        print('2. Remove Product')
        print('3. Update Stock')
        print('4. Update Price')
        print('5. Apply Discount')
        print('6. Show Reports')
        print('7. Export Data')
        print('8. Exit')

        try:
            user = int(input('Enter the options'))

            if user == 1:
                prodID = int(input('Enter the prod ID'))
                prodName = input('Enter the prod name')
                prodPrice = int(input('enter the prod price'))
                prodqty = int(input('enter the qty of the prod'))
                ctgyName = input('enter the category name')
                new_prod=Product(prodID, prodName, prodPrice, prodqty, ctgyName)
                store.add_product(new_prod)
                print('Product is added sccessfully')

            elif user == 2:
                prodID = int(input('enter the ID'))
                store.remove_product(prodID)
                print('Product is removed')

            elif user == 3:
                prodID = int(input('Enter the prod ID'))
                prodqty = int(input('enter the prod qty'))
                store.update_stock(prodID, prodqty)
                print('Product stock is updated')

            elif user == 4:
                prodID = int(input('enter the product id'))
                newprice = int(input('enter the new price'))
                store.update_price(prodID, newprice)
                print('Product price is updated')

            elif user == 5:
                ctyName = input('enter the category name')
                offpercentage = int(input('enter the percentage'))
                store.apply_discount_to_category(ctgyName, offpercentage)
                print('Discount is applied')

            elif user == 6:
                report = Report(store)
                report.total_inventory_value()
                report.category_summary()
                report.low_stock_items()

            elif user == 7:
                report = Report(store)

                report.export_to_json("MiniProject.json")
                report.export_to_csv("miniProject.csv")

            elif user == 8:
                print('Exit')
                break
        
            else:
                print('invalid options, Choice correct options')

        except Exception as e:
            print(f'Error: {e}')


if __name__ == "__main__":
    main()
