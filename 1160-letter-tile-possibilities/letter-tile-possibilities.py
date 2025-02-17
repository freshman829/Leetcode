from collections import Counter
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        def backtrack(tile_counter):
            combinations_count = 0

            for tile, count in tile_counter.items():
                if count > 0:
                    combinations_count += 1
                    tile_counter[tile] -= 1

                    combinations_count += backtrack(tile_counter)
                    tile_counter[tile] += 1
            return combinations_count
        
        tile_counter = Counter(tiles)
        return backtrack(tile_counter)


        
