# Parking-management-program
This Python code implements a basic parking management system. It allows users to record vehicle entries with license plate numbers and entry times, check if a vehicle is currently parked, and calculate parking fees upon exit based on the duration of stay. The system uses a dictionary to store active parking records.

🧾 Code Explanation
The ParkingManagement class manages parking operations with the following methods:

entry_car(car_plate, entry_time): Records the entry time of a vehicle identified by its license plate.

exit_car(car_plate): Calculates the duration a vehicle stayed in the parking lot and computes the parking fee based on a base cost and additional charges for extended hours.

parking_information(car_plate): Retrieves and displays the entry time of a specific vehicle.

add_car_info(): Prompts the user to input a vehicle's license plate and entry time, then records this information.

The system uses a dictionary (self.list_car) to store active parking records, mapping license plates to their corresponding entry times.

🎯 Purpose of the Code
This code serves as a foundational parking management system, suitable for small-scale parking facilities. It automates the process of tracking vehicle entries and exits and calculating parking fees, thereby reducing manual effort and minimizing errors. Such systems are essential for improving operational efficiency in parking lot management.
