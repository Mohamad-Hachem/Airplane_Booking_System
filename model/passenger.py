class Passenger:

    # initialization of class
    def __init__(self, passenger_id: int, first_name: str, last_name: str):
        self.passenger_id = passenger_id
        self.first_name = first_name
        self.last_name = last_name

    # how we would like to print
    def __str__(self):
        return (f"---------------------------------\n"
                f"Passenger information\n"
                f"Passenger_ID: {self.passenger_id}\nFirst_name: {self.first_name}\nLast_name: {self.last_name}\n"
                f"---------------------------------\n")

    # modifying first name
    def modifying_first_name(self, new_first_name):
        """
        this method allows you to modify first name
        it takes:
        :param new_first_name:
        :return: nothing(void)
        """
        self.first_name = new_first_name

    # modifying last name
    def modifying_last_name(self, new_last_name):
        """
        this method allows you to modify first name
        it takes:
        :param new_last_name:
        :return: nothing(void)
        """
        self.last_name = new_last_name
