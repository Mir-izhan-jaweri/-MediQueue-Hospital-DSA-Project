# ============================================
# DSA #3: GRAPH + BFS
# Real World Use: Hospital Navigation
# ============================================
# Problem: Emergency mein shortest path dhundna
#          (Main Entrance se ICU tak kaise jaayein)
# Solution: Graph + BFS (Breadth First Search)
# Time Complexity: O(V + E)
#   V = vertices (rooms), E = edges (corridors)
# ============================================

from collections import deque

# Hospital ka map — Graph (Adjacency List)
hospital_graph = {
    "Main Entrance": ["Parking", "Pharmacy", "Emergency Room"],
    "Parking":       ["Main Entrance", "Pharmacy"],
    "Pharmacy":      ["Main Entrance", "Parking", "Lab"],
    "Emergency Room":["Main Entrance", "ICU", "Lab"],
    "ICU":           ["Emergency Room", "Lab", "Ward A"],
    "Lab":           ["Pharmacy", "Emergency Room", "ICU", "OPD"],
    "Ward A":        ["ICU", "OPD"],
    "OPD":           ["Lab", "Ward A"],
}


def bfs_shortest_path(graph, start, end):
    """
    BFS se shortest path dhundo.

    Kaise kaam karta hai:
    1. Start room se shuru karo
    2. Uske sab neighbours check karo (level 1)
    3. Phir unke neighbours (level 2)
    4. Jab destination mile — ruk jao
    5. Yahi guaranteed shortest path hai!

    Time: O(V + E)
    Space: O(V)
    """
    if start == end:
        return [start]

    # Queue mein (current_room, path_so_far) store karo
    queue = deque()
    queue.append((start, [start]))

    # Visited rooms track karo — dobara mat jao
    visited = set([start])

    step = 0

    while queue:
        current_room, path = queue.popleft()
        step += 1

        print(f"  Step {step}: Checking '{current_room}' | Path so far: {' → '.join(path)}")

        # Is room ke sab neighbours check karo
        for neighbour in graph[current_room]:
            if neighbour not in visited:
                new_path = path + [neighbour]

                # Destination mil gaya!
                if neighbour == end:
                    print(f"\n✅ DESTINATION FOUND!")
                    return new_path

                visited.add(neighbour)
                queue.append((neighbour, new_path))

    print(f"❌ '{end}' tak koi rasta nahi mila!")
    return []


def dfs_all_paths(graph, start, end, path=None, visited=None):
    """
    DFS se SARE paths dhundo (comparison ke liye)
    DFS = Depth First Search — ek rasta poora explore karo
    """
    if path is None:
        path = [start]
    if visited is None:
        visited = set([start])

    if start == end:
        return [path]

    all_paths = []
    for neighbour in graph[start]:
        if neighbour not in visited:
            visited.add(neighbour)
            new_paths = dfs_all_paths(graph, neighbour, end, path + [neighbour], visited)
            all_paths.extend(new_paths)
            visited.remove(neighbour)

    return all_paths


def print_hospital_map(graph):
    """Hospital ka map print karo"""
    print("🏥 Hospital Map (Connections):")
    for room, neighbours in graph.items():
        print(f"  {room:20} ←→  {', '.join(neighbours)}")


# ============================================
# DEMO
# ============================================
if __name__ == "__main__":
    print("=" * 55)
    print("  HOSPITAL NAVIGATION SYSTEM")
    print("  DSA: Graph + BFS (Breadth First Search)")
    print("=" * 55)

    print_hospital_map(hospital_graph)

    # Test 1: Main Entrance se ICU
    print("\n" + "=" * 55)
    print("🚑 EMERGENCY: Main Entrance → ICU")
    print("=" * 55)
    print("\nBFS Search Steps:")
    path1 = bfs_shortest_path(hospital_graph, "Main Entrance", "ICU")
    if path1:
        print(f"\n📍 Shortest Path: {' → '.join(path1)}")
        print(f"   Total Stops: {len(path1) - 1}")

    # Test 2: Parking se Ward A
    print("\n" + "=" * 55)
    print("🏃 Parking → Ward A")
    print("=" * 55)
    print("\nBFS Search Steps:")
    path2 = bfs_shortest_path(hospital_graph, "Parking", "Ward A")
    if path2:
        print(f"\n📍 Shortest Path: {' → '.join(path2)}")
        print(f"   Total Stops: {len(path2) - 1}")

    # DFS se saare paths
    print("\n" + "=" * 55)
    print("🔍 DFS: Main Entrance se ICU ke SARE paths")
    print("=" * 55)
    all_p = dfs_all_paths(hospital_graph, "Main Entrance", "ICU")
    all_p.sort(key=len)
    for i, p in enumerate(all_p, 1):
        marker = " ← SHORTEST" if i == 1 else ""
        print(f"  Path {i} ({len(p)-1} stops): {' → '.join(p)}{marker}")

    print("\n--- BFS vs DFS ---")
    print("BFS: Level by level — GUARANTEED shortest path")
    print("DFS: Deep dive — finds ALL paths but not guaranteed shortest")
    print("\n--- Big-O ---")
    print("BFS Time: O(V + E)  where V=rooms, E=corridors")
    print("BFS Space: O(V)     visited set + queue")
