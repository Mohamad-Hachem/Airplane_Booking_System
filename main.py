import os
from model.airplanes import Airplanes
from model.reservations import Reservations
from model.passengers import Passengers
from utils.strings import (help_element, reservation_element, airplane_element, passenger_element, menu_element,
                           help_element_header)


def application():

    # starting the datastructures
    airplanes = Airplanes()
    reservations = Reservations()
    passengers = Passengers()

    # starting the program
    options = ""
    while options != "Q":
        # main menu
        print(menu_element)
        options = input("MAIN MENU:\n"
                        "Enter A to access airplanes panel\n"
                        "Enter P to access passenger panel\n"
                        "Enter R to access reservation panel\n"
                        "Enter H to know how does the airplane booking system work\n"
                        "Enter Q to Quit\n")
        options = options.upper()

        # refreshing the terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        match options:
            # TODO: Enter all airplane system action
            # Entering the airplane section
            case 'A':
                print(airplane_element)
                options_airplane = ""
                while options_airplane != "Q":
                    # airplane section menu
                    options_airplane = input("AIRPLANE MENU:\n"
                                             "Enter C to create a plane\n"
                                             "Enter M to modify a plane\n"
                                             "Enter D to delete a plane\n"
                                             "Enter P to print a plane\n"
                                             "Enter Q to back to main menu\n")

                    options_airplane = options_airplane.upper()
                    os.system('cls' if os.name == 'nt' else 'clear')

                    match options_airplane:
                        case 'C':
                            # creating airplane
                            print(airplane_element)
                            print(airplanes)
                            airplanes.create_airplane()
                            print("air plane was created\n")

                        case 'M':
                            # modifying airplane
                            print(airplane_element)
                            print(airplanes)
                            airplane_id = int(input("Please enter the ID of the plane you would like to modify:\n"))
                            airplanes.modifying_airplane_information(airplane_id)

                        case 'D':
                            # deleting airplane
                            print(airplane_element)
                            print(airplanes)
                            airplane_id = int(input("Please enter the ID of the plane you would like to delete\n"))
                            airplanes.delete_airplane(airplane_id)

                        case 'P':
                            # printing airplane
                            print(airplane_element)
                            print(airplanes)
                            airplane_id = int(input("Please enter the ID of the plane you would like to print\n"))
                            airplanes.print_airplane(airplane_id)
                        case 'Q':
                            pass
                        case _:
                            print(airplane_element)
                            print("Please enter a valid option")

            # TODO: Enter all passenger system action
            # Entering the passenger section
            case 'P':
                print(passenger_element)
                options_passenger = ""
                while options_passenger != "Q":
                    # passenger section Menu
                    options_passenger = input("PASSENGER MENU:\n"
                                              "Enter C to create a passenger\n"
                                              "Enter M to modify a passenger\n"
                                              "Enter D to delete a passenger\n"
                                              "Enter P to print a passenger\n"
                                              "Enter Q to back to main menu\n")

                    # clearing console
                    options_passenger = options_passenger.upper()
                    os.system('cls' if os.name == 'nt' else 'clear')

                    match options_passenger:
                        case 'C':
                            # creating passenger
                            print(passenger_element)
                            print(passengers)
                            passenger_id = int(input("Enter the new passenger ID:\n"))
                            if not passengers.does_passenger_exist(passenger_id):
                                passenger_first_name = input("Enter passenger first name:\n")
                                passenger_last_name = input("Enter passenger last name:\n")
                                passengers.add_passenger(passenger_id, passenger_first_name, passenger_last_name)
                            else:
                                print("Passenger with this ID already exist.\n")

                        case 'M':
                            # modifying passenger
                            print(passenger_element)
                            print(passengers)
                            passenger_id = int(input("Please enter the ID of the passenger you would like to modify:\n"))
                            passengers.modify_passenger(passenger_id)

                        case 'D':
                            # deleting passenger
                            print(passenger_element)
                            print(passengers)
                            passenger_id = int(input("Please enter the ID of the passenger you would like to delete\n"))
                            passengers.delete_passenger(passenger_id)

                        case 'P':
                            # printing passenger
                            print(passenger_element)
                            print(passengers)
                            printing_options = input("Enter 1 to print the passenger info\n"
                                                     "Enter 2 to print all the reservations of this passenger\n")

                            match printing_options:
                                case '1':
                                    # printing passenger info
                                    passenger_id = int(input("Please enter the ID of the passenger you would like to "
                                                             "print\n"))
                                    passengers.print_passenger_info(passenger_id)

                                case '2':
                                    # printing passenger reservations
                                    passenger_id = int(input("Please enter the ID of the passenger you would like to "
                                                     "print\n"))
                                    reservations.all_passenger_reservations(passenger_id)
                                case _:
                                    print("Enter a valuable option")

                        case 'Q':
                            pass
                        case _:
                            print(passenger_element)
                            print("Please enter a valid option")
                pass

            # TODO: Enter all reservation system action
            # Entering the reservation section
            case 'R':
                print(reservation_element)
                options_reservation = ""
                while options_reservation != "Q":
                    # reservation menu
                    options_reservation = input("RESERVATION MENU:\n"
                                                "Enter C to create a reservation\n"
                                                "Enter M to modify a reservation\n"
                                                "Enter D to delete a reservation\n"
                                                "Enter P to print a reservation\n"
                                                "Enter Q to back to main menu\n")

                    options_reservation = options_reservation.upper()
                    os.system('cls' if os.name == 'nt' else 'clear')

                    match options_reservation:
                        case 'C':
                            print(reservation_element)
                            print(reservations)
                            reservation_id = int(input("Enter the new reservation ID:\n"))

                            # To show available passenger
                            if not reservations.does_reservation_exists(reservation_id):
                                print(passengers)
                                passenger_id = int(input("Enter the passenger ID:\n"))

                                # making sure passenger exists
                                if passengers.does_passenger_exist(passenger_id):
                                    print(airplanes)
                                    airplane_id = int(input("Enter the id of the airplane to reserve in:\n"))
                                    if airplanes.does_airplane_exists(airplane_id):

                                        # choosing a seat on the plane
                                        airplanes.print_seat_on_plane(airplane_id)
                                        seat_id = int(input("Enter an available seat you would like to reserve:\n"))

                                        # making reservations
                                        if airplanes.airplanes_list[airplane_id].seat_allocator.is_seat_available(seat_id):
                                            airplanes.reserve_seat_on_plane(airplane_id, passenger_id, seat_id)
                                            reservations.create_reservation(reservation_id, airplane_id, passenger_id,
                                                                            seat_id)
                                        else:
                                            print("This seat is not available")
                                    else:
                                        print("Plane does not exist.\n")
                                else:
                                    print("This passenger does not exist.\n")
                            else:
                                print("This reservation ID exists already.\n")
                        case 'M':
                            print(reservation_element)
                            print(reservations)
                            reservation_id = int(input("Please enter the ID of the reservation you would like to "
                                                       "modify:\n"))
                            reservations.print_reservation(reservation_id)

                            if reservations.does_reservation_exists(reservation_id):
                                modifying_reservation_options = ""
                                while modifying_reservation_options != 'Q':

                                    modifying_reservation_options = input("Enter A to modify airplane\n"
                                                                          "Enter S to modify the seat\n"
                                                                          "Enter P to modify the passenger\n"
                                                                          "Enter Q to go back to reservation Menu\n")

                                    modifying_reservation_options = modifying_reservation_options.upper()

                                    match modifying_reservation_options:
                                        case 'A':
                                            print(airplanes)
                                            airplane_id = int(input("Enter your new airplane id:\n"))

                                            # checking if new airplane exist
                                            if airplanes.does_airplane_exists(airplane_id):

                                                # reserve new seat on new plane
                                                airplanes.print_seat_on_plane(airplane_id)
                                                new_seat_id = int(input("Enter the new seat ID you would like to "
                                                                        "reserve:\n"))
                                                passenger_id = reservations.reservation_list[reservation_id].passenger_id
                                                airplanes.airplanes_list[airplane_id].seat_allocator.reserve_seat(
                                                    passenger_id, new_seat_id)

                                                # release old seat from plane
                                                old_plane_id = reservations.reservation_list[reservation_id].airplane_id
                                                old_seat_id = reservations.reservation_list[reservation_id].seat_number

                                                airplanes.airplanes_list[old_plane_id].seat_allocator.release_seat(
                                                    old_seat_id)

                                                # making the final modification
                                                reservations.modify_reservation(reservation_id, airplane_id, passenger_id,
                                                                                new_seat_id)
                                            else:
                                                print("this airplane does not exist")
                                        case 'S':
                                            # getting needed info
                                            airplane_id = reservations.reservation_list[reservation_id].airplane_id
                                            old_seat_id = reservations.reservation_list[reservation_id].seat_number
                                            passenger_id = reservations.reservation_list[reservation_id].passenger_id

                                            # modifying seat
                                            airplanes.print_seat_on_plane(airplane_id)
                                            new_seat_id = int(input("Enter the new seat ID you would like to reserve:\n"))

                                            if airplanes.airplanes_list[airplane_id].seat_allocator.is_seat_available(
                                                    new_seat_id):

                                                airplanes.airplanes_list[airplane_id].seat_allocator.change_seat(
                                                    passenger_id, old_seat_id, new_seat_id)

                                                # making the final modification
                                                reservations.modify_reservation(reservation_id, airplane_id, passenger_id,
                                                                                new_seat_id)
                                            else:
                                                print("this seat is taken by someone else:\n")
                                        case 'P':
                                            # getting needed info
                                            airplane_id = reservations.reservation_list[reservation_id].airplane_id
                                            old_seat_id = reservations.reservation_list[reservation_id].seat_number
                                            passenger_id = reservations.reservation_list[reservation_id].passenger_id

                                            # changing passenger
                                            print(passengers)
                                            new_passenger_id = int(input("Enter passenger ID you would like to give the"
                                                                         "reservations for:\n"))

                                            # making the final modification
                                            if passengers.does_passenger_exist(new_passenger_id):

                                                reservations.modify_reservation(reservation_id, airplane_id,
                                                                                new_passenger_id,
                                                                                old_seat_id)
                                            else:
                                                print("The passenger doesn't exist:\n")
                                        case 'Q':
                                            pass
                                        case _:
                                            print("please include a valid options\n")

                            else:
                                print("This reservation does not exist please create one\n")
                        case 'D':
                            print(reservation_element)
                            print(reservations)
                            reservation_id_delete = int(input("Enter id of the reservation you would like to delete:\n"))
                            reservations.cancel_reservation(reservation_id_delete)
                        case 'P':
                            print(reservation_element)
                            print(reservations)
                            reservation_id = int(input("Enter the ID of reservation you would like to print:\n"))
                            reservations.print_reservation(reservation_id)
                        case 'Q':
                            pass
                        case _:
                            print(reservation_element)
                            print("Please enter a valid option:\n")

            # Entering the help section
            case 'H':
                print(help_element_header)
                print(help_element)

            # Exiting from the program
            case 'Q':
                pass

            case _:
                print("please enter a valid option")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application()
