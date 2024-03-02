# lab2.py
# Class section: CS 135
# Student Name: Ryan Harper
# Instructor Qiping Yan
# Assignment: Lab 2
# Submission Date: 3/1/2024
# References: https://realpython.com/python-f-strings/#writing-inline-comments
#
# Comments: Not sure exactly how the output is meant to be formatted so I just tried to make it nice
#


BASE_PRICE = 99
def main():
    # no input validation, anything that python can't force into an int will cause a crash
    packageNumber = int(input('Enter the number of packages you would like to purchase:')) 
    if not packageNumber > 0:
        print('You must purchase at least 1 package.')
        return
    if packageNumber < 10:
        discount = 0
    elif packageNumber >= 10 and packageNumber <= 19:
        discount = 0.1
    elif packageNumber >= 20 and packageNumber <=49:
        discount = 0.2
    elif packageNumber >= 50 and packageNumber <= 99:
        discount = 0.3
    elif packageNumber >= 100:
        discount = 0.4
    else:
        print('something went wrong... \n Exiting.')
        return
    priceBeforeDiscount = packageNumber * BASE_PRICE
    savings = priceBeforeDiscount * discount
    priceAfterDiscount = priceBeforeDiscount - savings
    trailingS = 's' if packageNumber > 1 else ''   # add an 's' if we have multiple packages, otherwise don't
    tmpStr = f' which means you saved ${savings:,.2f}!' if discount > 0 else '.' # only show savings if there actually are savings
    print(f'Since you bought {packageNumber} package{trailingS} you get a {discount:.0%} discount{tmpStr}')
    print(f'Your total price comes out to ${priceAfterDiscount:,.2f}')

if __name__ == '__main__':
    main()
