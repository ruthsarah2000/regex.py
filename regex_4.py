'''
Problem Statement:
You have a list of product descriptions. Your task is to tag each product based on keywords in the description. For instance, tag products 
as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.
'''

def tag_products(descriptions):
    tags = []
    for description in descriptions:
        if any(keyword in description.lower() for keyword in electronics_keywords):
            tags.append("Electronics")
        elif any(keyword in description.lower() for keyword in apparel_keywords):
            tags.append("Apparel")
        elif any(keyword in description.lower() for keyword in home_kitchen_keywords):
            tags.append("Home & Kitchen")
        else:
            tags.append("Other")
    return tags

electronics_keywords = {"smartphone", "tablet", "laptop", "tv", "camera"}
apparel_keywords = {"t-shirt", "shirt", "dress", "pants", "jeans"}
home_kitchen_keywords = {"kitchen", "cookware", "cutlery", "appliance", "home"}

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

tags = tag_products(descriptions)

for i, description in enumerate(descriptions):
    print(f"Product: {description} | Tag: {tags[i]}")

'''
Problem Statement:
You have a string containing various price formats from an international e-commerce site. Standardize all prices to the format 
'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.
'''
import re

def standardize_prices(price_data):
    
    patterns = [
        r'\$\d+\.\d+',  
        r'\d+\.\d+\s*USD',  
        r'\d+\.\d+\$',  
    ]
    
    for pattern in patterns:
        price_data = re.sub(pattern, 'USD XX.XX', price_data)
    
    return price_data


price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
standardized_prices = standardize_prices(price_data)

print(standardized_prices)
