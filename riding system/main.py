from users import Driver,Rider
from ride import Ride,RideMatching,RideRequest,RideSharing
from vehicle import Car,Bike


niye_jao=RideSharing("niye jao")
rider=Rider("rahim","rahim@gmail.com",102,"mohakhali",1200)
driver=Driver("kolim","kolim@gmail.com",202,"mohakhali")
niye_jao.add_rider(rider)
niye_jao.add_driver(driver)
rider.request_ride(niye_jao,"uttora","car")
driver.reached_destination(rider.current_ride)
rider.show_current_ride()
print(niye_jao)
