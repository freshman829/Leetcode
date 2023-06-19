class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_altitude = 0
        cur_altitude = 0
        for each_gain in gain:
            cur_altitude += each_gain
            if cur_altitude > highest_altitude:
                highest_altitude = cur_altitude
        return highest_altitude