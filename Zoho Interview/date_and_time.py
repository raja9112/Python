from datetime import datetime

def days_between_dates(date1, date2):
    # Parse the dates into datetime objects
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    
    # Calculate the absolute difference
    days = abs((d1-d2).days)
    return days

# Example Usage
date1 = "2024-11-18"
date2 = "2023-11-18"

print(days_between_dates(date1, date2))  # Output: 366

# Time and Space: O(1)