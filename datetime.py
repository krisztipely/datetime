from datetime import datetime

def print_current_datetime():
    """
    Print the current date and time.
    """
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_datetime}")

# Example usage:
print_current_datetime()
