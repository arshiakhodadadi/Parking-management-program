from datetime import datetime  

class ParkingManagement:  
    def __init__(self):  
        self.list_car = {} 

    def entry_car(self, car_plate, entry_time):  
        self.list_car[car_plate] = entry_time  
        print(f"Car with plate: {car_plate} at time: {entry_time} entered the parking lot")  

    def exit_car(self, car_plate):  
        try:  
            entry_time_str = self.list_car.pop(car_plate)  
            entry_time = datetime.strptime(entry_time_str, "%H:%M")  
            exit_time = datetime.now()   
            duration = (exit_time - entry_time).seconds / 3600   

            base_cost = 5000  
            if duration <= 6:  
                total_cost = base_cost  
            else:  
                extra_hours = duration - 6  
                total_cost = base_cost + (extra_hours * 1000)  

            print(f"Car with plate: {car_plate} left the parking lot.")  
            print(f"Total parking duration: {duration:.2f} hours")  
            print(f"Total cost: {total_cost:.2f} Toman")  
        except KeyError:  
            print(f"Car with plate: {car_plate} is not in the parking lot")  

    def parking_information(self, car_plate):  
        data = self.list_car.get(car_plate, 'This car is not available in the parking lot')  
        print(data)  

    def add_car_info(self):  
        car_plate = input("Enter the car license plate number: ")  
        entry_time = input("Enter the entry time (format HH:MM): ")  
        self.entry_car(car_plate, entry_time)  

 
parking_lot = ParkingManagement()  


parking_lot.add_car_info()  

car_plate_to_check = input("Enter the car license plate number to check its information: ")  
parking_lot.parking_information(car_plate_to_check)  
 
car_plate_to_exit = input("Enter the car license plate number to exit: ")  
parking_lot.exit_car(car_plate_to_exit)