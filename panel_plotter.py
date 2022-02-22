from typing import List, Tuple

class Plot_Panel:
    def __init__(self, coordinates:Tuple[int, int]) -> None:
        self.x, self.y = coordinates
        self.possible_edges:List[Plot_Panel] = []
        self.connections:List[Plot_Panel] = []
        self.incoming_connection:Plot_Panel = None

    def coordinates(self):
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f"P({self.x}, {self.y})"
    
    def __str__(self) -> str:
        return self.__repr__()

# List of panels to search through
panels:List[Plot_Panel] = []

# Finds panel which is at the tuple's location, None if none is found
def get_panel_at(coords:Tuple[int, int]) -> Plot_Panel | None:
    for panel in panels:
        if (panel.x, panel.y) == coords:
            return panel

    return None

# Selects which connections to make in order to have one continuos series
def make_tree(panel_coordinates:List[Tuple[int, int]]) -> None:
    global panels

    # make panels
    for tup in panel_coordinates:
        panels.append(Plot_Panel(tup))

    # make all available connections
    for panel in panels:
        l = get_panel_at((panel.x-1, panel.y))
        if not l is None:
            panel.possible_edges.append(l)

        r = get_panel_at((panel.x+1, panel.y))
        if not r is None:
            panel.possible_edges.append(r)

        ud = 1
        if (panel.x + panel.y) % 2 == 0:
            ud = -1
        
        udpanel = get_panel_at((panel.x, panel.y+ud))
        if not udpanel is None:
            panel.possible_edges.append(udpanel)


    # depth-first-search
    queue = [panel for panel in panels]
    panel = get_panel_at((0,0))
    queue.remove(panel)
    while len(queue) > 0:
        for edge in panel.possible_edges:
            if edge in queue and edge.incoming_connection == None:
                panel.connections.append(edge)
                edge.incoming_connection = panel
        panel = queue.pop(0)
    
    for panel in panels:
        print(f"{panel}: {panel.connections}")



def main():

    # data = [(-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1)]
    data = [(-1,0), (0,0), (1,0), (-1,1), (0,1), (1,1), (2,1),(2,2),(3,2),(4,2)]

    make_tree(data)

    return 0


if __name__ == '__main__':
    main()