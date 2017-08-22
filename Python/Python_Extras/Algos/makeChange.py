import math

def change(cents):
    coins = {'dollars': 0, 'half-dollars': 0, 'quarters': 0, 'dimes': 0, 'nickels': 0, 'pennies': 0}
    if cents%100 != 0:
        coins['dollars'] = math.floor(cents/100)
        cents = cents%100
        if cents%50 != 0:
            coins['half-dollars'] = math.floor(cents/50)
            cents = cents%50
            if cents%25 != 0:
                coins['quarters'] = math.floor(cents/25)
                cents = cents%25
                if cents%10 != 0:
                    coins['dimes'] = math.floor(cents/10)
                    cents = cents%10
                    if cents%5 != 0:
                        coins['nickels'] = math.floor(cents/5)
                        cents = cents%5
                        coins['pennies'] = cents
                    else:
                        coins['nickels'] = cents/5
                else:
                    coins['dimes'] = cents/10
            else:
                coins['quarters'] = cents/25
        else:
            coins['half-dollars'] = cents/50
    else:
        coins['dollars'] = cents/100
    return coins

test = change(387)
print test
