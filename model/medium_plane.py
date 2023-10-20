from model.airplane import Airplane
from model.seat_allocator import SeatAllocator
from datetime import time


class MediumPlane(Airplane):

    # initialization of class
    def __init__(self, airplane_id: int, company_name: str, departure_time: time, arrival_time: time):
        super().__init__(airplane_id, company_name, departure_time, arrival_time)
        self.seat_allocator = SeatAllocator(8)

    # how we would like to print
    def __str__(self):
        base_str = super().__str__()
        return base_str + f"{self.seat_allocator}\n---------------------------\n"

