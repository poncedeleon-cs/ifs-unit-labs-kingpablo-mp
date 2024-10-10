# Name: Matthew Park
# Period: 6th
#

# define a function getDiscountedPrice() that takes the original prince as a
# parameter and returns the price of the item after the discount is applied.
def getDiscountedPrice(price):
    if price>2000:
        newprice = price - (price*0.1)
        return newprice
    else:
        return price
