# transform_string

from collections import deque

def transform_string(start, end, rules):
    if start == end:
        return 0  # No transformation needed if both are already the same

    # Convert rules into a graph
    graph = {}
    for rule in rules:
        a, b = rule
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    # BFS to find the minimum transformation steps
    queue = deque([(start, 0)])  # (current_string, current_steps)
    visited = set([start])

    while queue:
        current, steps = queue.popleft()

        for i in range(len(current)):
            for neighbor in graph.get(current[i], []):
                transformed = current[:i] + neighbor + current[i+1:]
                if transformed == end:
                    return steps + 1
                if transformed not in visited:
                    visited.add(transformed)
                    queue.append((transformed, steps + 1))

    return "Impossible"  # No transformation found

# Example usage:
start = "abc"
end = "def"
rules = [["a", "d"], ["b", "e"], ["c", "f"]]
print(transform_string(start, end, rules))  # Output: 3

start = "abc"
end = "xyz"
rules = [["a", "d"], ["b", "e"], ["c", "f"]]
print(transform_string(start, end, rules))  # Output: Impossible
