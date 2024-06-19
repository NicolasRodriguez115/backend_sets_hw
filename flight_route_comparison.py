from main import our_routes
from main import competitor_routes

def route_comparison():
    destinations_both = our_routes.intersection(competitor_routes)
    print(destinations_both)
    our_unique_destinations = our_routes.difference(competitor_routes)
    print (our_unique_destinations)
    unique_destinations = our_routes.symmetric_difference(competitor_routes)
    print(unique_destinations)