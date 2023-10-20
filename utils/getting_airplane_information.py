from datetime import datetime, time
from typing import Dict


# getting info from administrator
def getting_payload() -> Dict:
    """
    this function takes nothing and return a dictionary of the users answers
    :return: id, company_name, departure_time, arrival_time
    """
    temp_id = int(input("Enter the plane ID(int):\n"))
    temp_company_name = input("Enter the company name:\n")

    # making sure time is in the correct format
    try:
        temp_departure_time = input("Enter the departure time => (hh:mm:ss) example, (14:05:20):\n")
        temp_departure_time = datetime.strptime(temp_departure_time, "%H:%M:%S").time()
    except ValueError:
        print("You have entered time in the wrong Format, the system will assign the time to\n"
              "1:1:1 instead. Feel free to modify the departure time in plane modification")
        temp_departure_time = time(1, 1, 1)

    # making sure time is in the correct format
    try:
        temp_arrival_time = input("Enter the arrival time => (hh:mm:ss) example, (14:05:20):\n")
        temp_arrival_time = datetime.strptime(temp_arrival_time, "%H:%M:%S").time()
    except ValueError:
        print("You have entered time in the wrong Format, the system will assign the time to\n"
              "1:1:1 instead. Feel free to modify the arrival time in plane modification")
        temp_arrival_time = time(1, 1, 1)

    return {
        "id": temp_id,
        "company_name": temp_company_name,
        "departure_time": temp_departure_time,
        "arrival_time": temp_arrival_time
    }
