def calculate_discounted_price(price, discount_percentage):
    """
    Calculate the discounted price given the original price and discount percentage.

    Parameters:
    price (float): The original price of the item.
    discount_percentage (float): The discount percentage to be applied.

    Returns:
    float: The price after applying the discount.
    """
      

print("Welcome to the Discount Calculator!")
price = float(input("Enter the original price of the item: ")) 
if price < 0:
    print("Original price cannot be negative.")
    exit()
discount_percentage = float(input("Enter the discount percentage: ")) 
if discount_percentage < 0 or discount_percentage > 100:
    print("Discount percentage must be between 0 and 100.")
if discount_percentage == 0:
    print(f"No discount applied. The price remains: ${price:.2f} ")
    exit()
discount_amount = (discount_percentage / 100) * price
discounted_price = price - discount_amount
print(f"The discount amount is: ${discount_amount:.2f}")    
print(f"The price after a {discount_percentage}% discount is: ${discounted_price:.2f}")





 
 

 
 
















