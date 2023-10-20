from datetime import time


class Airplane:

    # initialization of class
    def __init__(self, airplane_id: int, company_name: str, departure_time: time, arrival_time: time):
        self.airplane_id = airplane_id
        self.company_name = company_name
        self.departure_time = departure_time
        self.arrival_time = arrival_time

    # how we would like to print
    def __str__(self):
        return (f"---------------------------\n"
                f"Airplane details:\nID: {self.airplane_id}\nCompany Name: {self.company_name}\nDeparture Time: "
                f"{self.departure_time} \nArrival Time: {self.arrival_time}\n"
                f"---------------------------\n")

    # changing airplane name
    def change_airplane_name(self, new_company_name: str) -> None:
        """
        This method takes a  (new_company_name) and change the original
        :param new_company_name:
        :return: nothing(void)
        """
        self.company_name = new_company_name

    # changing departure time
    def change_departure_time(self, new_departure_time: time) -> None:
        """
        This method takes a time (new_departure_time) and change the original
        :param new_departure_time:
        :return: nothing(void)
        """
        self.departure_time = new_departure_time

    def change_arrival_time(self, new_arrival_time: time) -> None:
        """
        This method takes a time (new_arrival_time) and change the original
        :param new_arrival_time:
        :return: nothing(void)
        """
        self.arrival_time = new_arrival_time
