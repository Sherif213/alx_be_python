from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date)
    
def calculate_future_date(day):
    future_date = (datetime.now() + timedelta(days=day)).date()
    
    print(future_date)
    
display_current_datetime()
calculate_future_date(10)