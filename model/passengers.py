from model.passenger import Passenger


class Passengers:

    # initialization of class
    def __init__(self):
        self.passengers_list = {}

    # how we would like to print
    def __str__(self):
        return f"List of passenger ID {[i for i in self.passengers_list]}"

    # does passenger exist
    def does_passenger_exist(self, passenger_id: int) -> bool:
        """
        This method allows you to check if a passenger exist already or not
        it takes
        :param passenger_id:
        :return: bool
        """
        return passenger_id in self.passengers_list.keys()

    # adding passenger to the list
    def add_passenger(self, passenger_id: int, first_name: str, last_name: str) -> None:
        """
        this method allows you to add a passenger to the list
        it takes
        :param passenger_id:
        :param first_name:
        :param last_name:
        :return: nothing(void)
        """
        if self.does_passenger_exist(passenger_id):
            print("a passenger with this id already exists")
        else:
            self.passengers_list[passenger_id] = Passenger(passenger_id, first_name, last_name)

    # modify passenger information
    def modify_passenger(self, passenger_id: int) -> None:
        """
        This method allows you to choose what you want to modify in a passenger
        it takes:
        :param passenger_id:
        :return: nothing(void)
        """
        if self.does_passenger_exist(passenger_id):
            modifying_passenger_option = input("Enter F to modify first name\n"
                                               "Enter L to modify last name\n"
                                               "Enter Q to exit\n")

            modifying_passenger_option = modifying_passenger_option.upper()

            match modifying_passenger_option:
                case 'F':
                    new_first_name = input("Enter new first name\n")
                    self.passengers_list[passenger_id].modifying_first_name(new_first_name)
                case 'L':
                    new_last_name = input("Enter new last name\n")
                    self.passengers_list[passenger_id].modifying_last_name(new_last_name)
                case 'Q':
                    pass
                case _:
                    print("Please Enter a valid command")
                    self.modify_passenger(passenger_id)
        else:
            print("This passenger does not exist, create one first")

    # delete a passenger
    def delete_passenger(self, delete_passenger_id: int) -> None:
        """
        This method allows you to delete an existing passenger
        it takes
        :param delete_passenger_id:
        :return: nothing(void)
        """
        if self.does_passenger_exist(delete_passenger_id):
            self.passengers_list.pop(delete_passenger_id)
            print(f"the passenger with id {delete_passenger_id} is deleted")
        else:
            print("This passenger does not exist")

    # print a passenger info
    def print_passenger_info(self, passenger_id) -> None:
        """
        this method allows you to print the information of a passenger
        it takes
        :param passenger_id:
        :return: nothing(void)
        """
        if self.does_passenger_exist(passenger_id):
            print(self.passengers_list[passenger_id])
        else:
            print("This passenger does not exist")
