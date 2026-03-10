# Depth-First Search (DFS)

class MachineNetwork:
    def __init__(self):
        self.machine_links = {}

    def add_machine(self, machine):
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        self.add_machine(m1)
        self.add_machine(m2)
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        print("Machine Network:")
        for machine, links in self.machine_links.items():
            print(f"{machine}: {links}")

    def print_connected_machines(self, machine):
        if machine in self.machine_links:
            print(f"Machines connected to {machine}: {self.machine_links[machine]}")
        else:
            print(f"Machine {machine} does not exist in the network.")

    def bfs(self, start):
        if start not in self.machine_links:
            print(f"Machine {start} not found.")
            return []

        visited = []
        queue = [start]

        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
                for neighbor in self.machine_links[current]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        return visited

    def dfs(self, start):
        """Depth-First Search (DFS) starting from 'start' machine."""
        if start not in self.machine_links:
            print(f"Machine {start} not found.")
            return []

        visited = []
        stack = [start]

        while stack:
            current = stack.pop()  # remove from end (stack behavior)
            if current not in visited:
                visited.append(current)
                # Add neighbors in reverse to keep order similar to adjacency list
                for neighbor in reversed(self.machine_links[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited


# Testing Exercise 3
network = MachineNetwork()

# Add the same links as before
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
print()

# DFS from Machine_A
print("DFS from Machine_A:", network.dfs("Machine_A"))