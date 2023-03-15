from abc import ABC, abstractmethod
from serviceable import Serviceable
from datetime import datetime,date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class Car(Serviceable, ABC):
    def __init__(self, engine, battery):
        self.__engine = engine
        self.__battery = battery

    def needs_service(self):
        return self.__battery.needs_service() or self.__engine.needs_service()


class CarFactory(ABC):
    @staticmethod
    def create_calliope(self, current_date:datetime,last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        return Car(engine=engine,battery=battery)
    
    @staticmethod
    def create_glissade(self, current_date:datetime,last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        return Car(engine=engine,battery=battery)
        
    @staticmethod
    def create_palindrome(self, current_date:datetime,last_service_date: datetime, warning_light_is_on: bool) -> Car:
        
        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        battery = SpindlerBattery(last_service_date=last_service_date,current_date=current_date)
        return Car(engine=engine,battery=battery)
        
    @staticmethod
    def create_rorschach(self, current_date:datetime,last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date,current_date=current_date)
        return Car(engine=engine,battery=battery)
    
    @staticmethod
    def create_thovex(self, current_date:datetime,last_service_date: datetime, current_mileage: int, last_service_mileage: int) -> Car:
        
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        battery = NubbinBattery(last_service_date=last_service_date,current_date=current_date)
        return Car(engine=engine,battery=battery)
    

