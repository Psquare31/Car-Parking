class Car:
    def __init__(self,car_number,car_type,entry_time):
        self.car_number=car_number
        self.car_type=car_type
        self.entry_time=entry_time
        
        
class ParkingSlot:
    def _init_(self, slot_id, is_occupied, car):
        self.slot_id = slot_id
        self.is_occupied = is_occupied
        self.car = car
        
class ParkingLot:
    def _init_self(self, total_slot, available_slot, slots, active_ticket):
        self.total_slot = total_slot
        self.available_slot = available_slot
        self.slot = slots
        self.active_ticket = active_ticket
        

class Ticket:
    def _init_self(self, ticket_id, car_number, slot_id, entry_time, exit_time):
        self.ticket_id = ticket_id
        self.car_number = car_number
        self.slot_id = slot_id
        self.entry_time = entry_time
        self.exit_time = exit_time