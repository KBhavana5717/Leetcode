class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)   # closest to target first

        fleets = 0
        slowest_time = 0.0       # arrival time of the fleet directly ahead

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets