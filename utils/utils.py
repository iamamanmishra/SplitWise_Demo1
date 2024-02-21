from datetime import datetime


def get_concatenated_datetime():
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the current date and time as a concatenated string
    concatenated_datetime = current_datetime.strftime("%Y%m%d%H%M%S")

    return str(concatenated_datetime)


def get_current_date():
    # Get the current date
    current_date = datetime.now().strftime("%Y-%m-%d")

    return current_date


# # Example usage
# print(get_current_date())
#
# # Example usage
# print(get_concatenated_datetime())
