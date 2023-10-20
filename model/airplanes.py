from model.small_plane import SmallPlane
from model.medium_plane import MediumPlane
from model.large_plane import LargePlane
from utils.getting_airplane_information import getting_payload


class Airplanes:

    # initialization of class
    def __init__(self):
        self.airplanes_list = {}

    # how we would like to print
    def __str__(self):
        return f"List of airplanes IDs: {[i for i in self.airplanes_list]}"

    # creating an airplane
    def create_airplane(self) -> None:
        """
        This method creates a plane and stores it into the airplanes_list
        you can choose to create S small, M medium, L Large, planes
        :return: nothing(void)
        """
        # choosing S, M, or L to create a plane
        choosing_airplane_type = input("Enter S to create small plane\n"
                                       "Enter M to create Medium plane\n"
                                       "Enter L to create Large plane\n"
                                       "Enter Q to quit\n")

        choosing_airplane_type = choosing_airplane_type.upper()

        match choosing_airplane_type:
            case 'S':
                temp = getting_payload()
                temp_plane = SmallPlane(temp['id'], temp['company_name'], temp['departure_time'], temp['arrival_time'])
                self.airplanes_list[temp_plane.airplane_id] = temp_plane
            case 'M':
                temp = getting_payload()
                temp_plane = MediumPlane(temp['id'], temp['company_name'], temp['departure_time'], temp['arrival_time'])
                self.airplanes_list[temp_plane.airplane_id] = temp_plane
            case 'L':
                temp = getting_payload()
                temp_plane = LargePlane(temp['id'], temp['company_name'], temp['departure_time'], temp['arrival_time'])
                self.airplanes_list[temp_plane.airplane_id] = temp_plane
            case 'Q':
                pass
            case _:
                print("You have entered an Invalid command please try again\n")
                self.create_airplane()

    # does airplane exists
    def does_airplane_exists(self, exists_airplane_id) -> bool:
        """
        This method makes sure that the airplane already exists
        it takes:
        :param exists_airplane_id:
        :return: bool
        """
        return exists_airplane_id in self.airplanes_list.keys()

    # modifying airplanes
    def modifying_airplane_information(self, modify_airplane_id: int) -> None:
        """
        This method allows the administrator to modify an airplane information such as
        company_name, arrival_time, departure_time, ID of then plane is not allowed to change
        :param modify_airplane_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(modify_airplane_id):
            choosing_modification_type = input("Enter N to modify the name of the company\n"
                                               "Enter D to modify the departure time of the plane\n"
                                               "Enter A to modify the arrival time of the plane\n"
                                               "Enter Q to quit\n")

            choosing_modification_type = choosing_modification_type.upper()

            match choosing_modification_type:
                case 'N':
                    new_company_name = input("Enter the new name of the company\n")
                    self.airplanes_list[modify_airplane_id].change_airplane_name(new_company_name)
                case 'D':
                    new_departure_time = input("Enter the new departure time format -> hh:mm:ss\n")
                    self.airplanes_list[modify_airplane_id].change_departure_time(new_departure_time)
                case 'A':
                    new_arrival_time = input("Enter the new departure time format -> hh:mm:ss\n")
                    self.airplanes_list[modify_airplane_id].change_arrival_time(new_arrival_time)
                case 'Q':
                    pass
                case _:
                    print("You have entered an Invalid command please try again\n")
        else:
            print("This airplane does not exists create one or enter an airplane that exists")

    # deleting an airplanes
    def delete_airplane(self, delete_airplane_id: int) -> None:
        """
        This method will delete an existing airplane
        it takes:
        :param delete_airplane_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(delete_airplane_id):
            self.airplanes_list.pop(delete_airplane_id)
            print(f"the airplane with id: {delete_airplane_id} is deleted successfully")
        else:
            print("This airplane does not exists")

    # print a specific airplane
    def print_airplane(self, print_airplane_id: int) -> None:
        """
        This method will print any airplane in the list
        it takes:
        :param print_airplane_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(print_airplane_id):
            print(self.airplanes_list[print_airplane_id])
        else:
            print("This plane does not exists")

    # reserve a seat on a certain plane
    def reserve_seat_on_plane(self, reserve_seat_airplane_id: int, passenger_id: int, seat_id: int) -> None:
        """
        This method allows you to reserve a seat for a passenger on a specific airplane
        :param reserve_seat_airplane_id:
        :param passenger_id:
        :param seat_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(reserve_seat_airplane_id):
            self.airplanes_list[reserve_seat_airplane_id].seat_allocator.reserve_seat(passenger_id, seat_id)
        else:
            print("This plane does not exists")

    # change a seat on a certain plane
    def change_seat_on_plane(self, change_seat_airplane_id: int, passenger_id: int, seat_id_current_taken: int,
                             new_seat_id: int) -> None:
        """
        This method allows you to change a seat of a passenger on an already existing plane
        it takes:
        :param change_seat_airplane_id:
        :param passenger_id:
        :param seat_id_current_taken:
        :param new_seat_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(change_seat_airplane_id):
            self.airplanes_list[change_seat_airplane_id].seat_allocator.change_seat(passenger_id, seat_id_current_taken,
                                                                                    new_seat_id)
        else:
            print("This plane does not exists")

    # release a seat on a certain plane
    def release_seat_on_plane(self, release_seat_airplane_id: int, seat_id: int) -> None:
        """
        This method allows you to release(make it available) a seat no a specific plane
        :param release_seat_airplane_id:
        :param seat_id:
        :return:nothing(void)
        """
        if self.does_airplane_exists(release_seat_airplane_id):
            self.airplanes_list[release_seat_airplane_id].seat_allocator.release_seat(seat_id)
        else:
            print("This plane does not exists")

    # print a plane's seats
    def print_seat_on_plane(self, print_airplane_id: int) -> None:
        """
        this method will print the seats of a plane
        :param print_airplane_id:
        :return: nothing(void)
        """
        if self.does_airplane_exists(print_airplane_id):
            print(self.airplanes_list[print_airplane_id].seat_allocator)
        else:
            print("This plane does not exists")
