'''
An underground railway system keeps track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:


void checkIn(int id, string stationName, int t)

A customer with a card ID equal to id, checks in at the station stationName at time t. A customer can only be checked into one place at a time.


void checkOut(int id, string stationName, int t)

A customer with a card ID equal to id, checks out from the station stationName at time t.


double getAverageTime(string startStation, string endStation)

Returns the average time it takes to travel from startStation to endStation.


The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check-in at startStation followed by a check-out from endStation.
The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12
'''


class Customer:
    def __init__(self):
        self.id: int
        self.check_in_station_name: str
        self.check_out_station_name: str
        self.check_in_time: int
        self.check_out_time: int


class UndergroundSystem:

    def __init__(self):
        self.avg_time_storage: dict[str, list[int]] = {}
        self.trip_storage: dict[int, dict[str, int]] = {}

    def checkIn(self, id: int, station_name: str, t: int):
        """
        A customer with a card ID equal to id, checks in at the station station_name at time t. A customer can only be checked into one place at a time.
        """
        self.trip_storage[id]["checkIn"] = t


    def checkOut(self, id: int, station_name: str, t: int):
        """
        A customer with a card ID equal to id, checks out from the station station_name at time t.
        """
        pass

    def getAverageTime(self, start_station_name: str, end_station_name: str) -> int:
        """
        Returns the average time it takes to travel from start_station_name to end_station_name.
        """
        if not self.avg_time_storage[f"{start_station_name}+{end_station_name}"]:
            self.avg_time_storage[f"{start_station_name}+{end_station_name}"] = []
        self.avg_time_storage[f"{start_station_name}+{end_station_name}"].append()
