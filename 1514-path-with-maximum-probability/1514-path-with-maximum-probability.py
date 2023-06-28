class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Step 1: Create adjacency list
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            p = succProb[i]
            graph[a].append((b, p))
            graph[b].append((a, p))

        # Step 2: Initialize distance array
        dist = [0] * n
        dist[start] = 1

        # Step 3: Initialize priority queue
        pq = []
        heapq.heappush(pq, (-1, start))  # Use negative probability for a min-heap

        # Step 5: Dijkstra's algorithm
        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob  # Restore the positive probability

            if node == end:
                return prob

            if prob < dist[node]:
                continue

            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob

                if new_prob > dist[neighbor]:
                    dist[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        # Step 6: No path from start to end
        return 0
        