# Create the Machine Network Graph
class MachineNetwork:
    def __init__(self):
        # key = machine, value = list of connected machines
        self.machine_links = {}

    def add_machine(self, machine):
        """Add a machine to the network if it doesn't exist yet."""
        if machine not in self.machine_links:
            self.machine_links[machine] = []

    def add_link(self, m1, m2):
        """Connect two machines (both directions)."""
        # Ensure both machines exist
        self.add_machine(m1)
        self.add_machine(m2)
        # Add link in both directions if not already present
        if m2 not in self.machine_links[m1]:
            self.machine_links[m1].append(m2)
        if m1 not in self.machine_links[m2]:
            self.machine_links[m2].append(m1)

    def print_network(self):
        """Print all machines and their connections."""
        print("Machine Network:")
        for machine, links in self.machine_links.items():
            print(f"{machine}: {links}")

    def print_connected_machines(self, machine):
        """Print machines directly connected to a given machine."""
        if machine in self.machine_links:
            print(f"Machines connected to {machine}: {self.machine_links[machine]}")
        else:
            print(f"Machine {machine} does not exist in the network.")


# Testing Exercise 1
network = MachineNetwork()

# Add the specific links from the assignment
network.add_link("Machine_A", "Machine_B")
network.add_link("Machine_A", "Machine_C")
network.add_link("Machine_B", "Machine_D")
network.add_link("Machine_C", "Machine_D")
network.add_link("Machine_C", "Machine_E")

network.print_network()
print()
network.print_connected_machines("Machine_C")