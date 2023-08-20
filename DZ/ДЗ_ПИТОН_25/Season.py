from Serials import *

class Season:
    
    def __init__(self, count_season:int=1, series:list=[]):
        self.__count_season =  count_season
        self.__list_of_series = []
        for serie in series: #serie - object of Serials
            self.__list_of_series.append(serie) # list of series
    
    def show_series(self):
        for serie in self.__list_of_series: #serie - object of Serials
            print(self.__list_of_series.index(serie)+1,serie.name)

    
