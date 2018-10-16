"""
This program implements a bid allocation algorithm similar to that
described in Google's S-1 assuming a pro rata allocation.

A bid is a tuple of:
 - bidder ID (a unique string)
 - the number of items you are interested in purchasing
 - the price per item you are willing to pay

see <http://jtauber.com/blog/2004/04/30/google_auction_in_python>

"""

def process_bids(number_offered, bids):
    """
    Process the given list of bids with the given number of items being offered.

    Returns a list of tuples, one for each successful bidder:
     - bidder ID
     - the number of items received
     - the price sold at
    """
    
    # sort bids by descending price
    bids.sort(lambda a, b: -cmp(a[2], b[2]))

    # find successful bidders
    successful_bids = []
    total_number = 0
    for bid in bids:
        if total_number > number_offered:
            break
        successful_bids.append(bid)
        total_number += bid[1]

    # calculate price from last successful bidder
    price = successful_bids[-1][2]

    pro_rate_allocation = float(number_offered) / total_number

    return [(bid[0], round(bid[1] * pro_rate_allocation), price) for bid in successful_bids]


## EXAMPLE

bids = [("A", 100, 30), ("B", 2100, 28), ("C", 4000, 26),
        ("D", 4500, 24), ("E", 5000, 22), ("F", 5500, 20),
        ("G", 1000, 18), ("H", 2000, 16)]

print process_bids(20000, bids)
