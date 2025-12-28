import time



class Car:
    def __init__(self, vehicle_number, vehicle_type, entry_time, estimated_exit_time):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.entry_time = entry_time
        self.estimated_exit_time = estimated_exit_time
        
        
class ParkingSlot:
    def __init__(self, slot_id, is_occupied, vehicle):
        self.slot_id = slot_id
        self.is_occupied = is_occupied
        self.vehicle = vehicle
        
class ParkingLot:
    def __init__(self, total_slot, available_slot, slots, active_ticket):
        self.total_slot = total_slot
        self.available_slot = available_slot
        self.slots = slots
        self.active_ticket = active_ticket
        

class Ticket:
    def __init__(self, ticket_id, vehicle_number, slot_id, entry_time, exit_time):
        self.ticket_id = ticket_id
        self.vehicle_number = vehicle_number
        self.slot_id = slot_id
        self.entry_time = entry_time
        self.exit_time = exit_time

  
lock = False
slots = []
tickets = []
rnpn_enterprises = ParkingLot(100, 100, slots, 0)


for i in range(rnpn_enterprises.total_slot):
    slot = ParkingSlot(slot_id = i, is_occupied = False, vehicle = None)
    break
    

def vehicle_entry(slot, vehicle, parkingLot):
    slot.is_occupied = True
    slot.vehicle = vehicle
            
    new_ticket = Ticket(slot.slot_id + 10, vehicle.vehicle_number, vehicle.entry_time, vehicle.entry_time)
    tickets.append(new_ticket)
    
    parkingLot.active_ticket += 1
    parkingLot.available_slot -= 1
    
def vehicle_exit(slot, vehicle, parkingLot):
    global lock
    
    slot.is_occupied = False
    slot.vehicle = None
    
    for ti in tickets:
        if ti.slot_id == slot.slot_id:
            del ti
            break
            
    parkingLot.active_ticket -= 1
    parkingLot.available_slot += 1
    lock = False
    

while not lock:
    if rnpn_enterprises.available_slot > 0:
        for i in rnpn_enterprises.slots:
            if not i.is_occupied:
                vehicle_number = input("Enter vehicle Number: ")
                vehicle_type = input("Enter Vehicle Type: ")
                vehicle_entry_time = time.time()
                estimated_exit_time = int(input("Enter Estimated Exit Time in Hours: "))
                exit_time = vehicle_entry_time + (estimated_exit_time*3600)
    
                new_Vehicle = Car(vehicle_number, vehicle_type, vehicle_entry_time, exit_time)
                
                vehicle_entry(i, new_Vehicle, rnpn_enterprises)
            else:
                print("Parking Lot is FULL..!!")
                lock = True
