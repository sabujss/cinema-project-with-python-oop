from datetime import datetime as dt
from vehicle import Car,Bike

class RideSharing:
    def __init__(self,company_name):
        self.company_name=company_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    
    def __repr__(self):
        return f"(ride sharing company:{self.company_name}\t\twith rider: {len(self.riders)}\t\tand with driver: {len(self.drivers)})"


class Ride:
    def __init__(self,start_location,end_location,vehicle):
        self.start_location=start_location
        self.end_location=end_location
        self.start_time=None
        self.end_time=None
        self.driver=None
        self.rider=None
        self.estimated_fare=self.calculate_fare(vehicle.vehicle_type)
        self.vehicle=vehicle
        
    def set_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=dt.now()

    def end_ride(self):
        self.end_time=dt.now()
        self.driver.wallet+=self.estimated_fare
        self.rider.wallet-=self.estimated_fare
        
    def calculate_fare(self,vehicle_type):
        distance=10
        fare_per_km={
            "car":30,
            "bike":25,
            "cng":20
        }
        return distance*fare_per_km[vehicle_type]

    def __repr__(self):
        return f"start ride : {self.start_location} to {self.end_location}"

class RideRequest:
    def __init__(self,rider,end_location):
        self.rider=rider
        self.end_location=end_location

class RideMatching:
    def __init__(self,driver):
        self.available_driver=driver
    
    def find_driver(self,ride_request,vehicle_type):
        if len(self.available_driver)>0:
            print("Looking drivers.........")
            driver=self.available_driver[0]

            if vehicle_type=="car":
                vehicle=Car("car","123s5",30)
            elif vehicle_type=="bike":
                vehicle=Bike("motor bike","123ss1",50)
            
            ride=Ride(ride_request.rider.current_location,ride_request.end_location,vehicle)

            driver.accept_ride(ride)
            return ride
        

        
