class Car:
    def __init__(self, car_number, car_type, entry_time, estimated_exit_time):
        self.car_number = car_number
        self.car_type = car_type
        self.entry_time = entry_time
        self.estimated_exit_time = estimated_exit_time
        
        
class ParkingSlot:
    def __init__(self, slot_id, is_occupied, car):
        self.slot_id = slot_id
        self.is_occupied = is_occupied
        self.car = car
        
class ParkingLot:
    def __init__(self, total_slot, available_slot, slots, active_ticket):
        self.total_slot = total_slot
        self.available_slot = available_slot
        self.slots = slots
        self.active_ticket = active_ticket
        

class Ticket:
    def __init__(self, ticket_id, car_number, slot_id, entry_time, exit_time):
        self.ticket_id = ticket_id
        self.car_number = car_number
        self.slot_id = slot_id
        self.entry_time = entry_time
        self.exit_time = exit_time
        

slots = []
rnpn_enterprises = ParkingLot(100, 100, slots, 0)


for i in range(rnpn_enterprises.total_slot):
    slot = ParkingSlot(slot_id = i, is_occupied = False, car = None)
    
BMW = Car('BR06969', 'Jeep', '10:00 AM', '02:00 PM')


def car_entry(slot, car, parkingLot):
    slot.is_occupied = True
    slot.car = car
            
    new_ticket = Ticket(slot.slot_id + 10, car.car_number, car.entry_time, car.entry_time)
    parkingLot.active_ticket += 1
    parkingLot.available_slot -= 1
    
if rnpn_enterprises.available_slot > 0:
    for i in rnpn_enterprises.slots:
        if not i.is_occupied:
            car_entry(i, BMW, rnpn_enterprises)
    
else:
    print("Parking Lot is FULL..!! Jaam")

