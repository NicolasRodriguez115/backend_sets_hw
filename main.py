our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
def main():
    from flight_route_comparison import route_comparison
    from unique_customer_ids import unique_ids
    # Lesson 3: Assignments | Sets
    # 1. Python Sets Adventure
    route_comparison()
    # Task 1: Flight Route Comparison
    unique_ids()

if __name__ == "__main__":
    main()