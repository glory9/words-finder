class Compass:
    def __init__(self, start=0):
        self.current_direction = start
        self.directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    def get_curr_index_changes(self, current_direction=None):
        current_direction = current_direction if current_direction else self.current_direction
        changes = self.directions[current_direction]
        self.current_direction += 1
        self.current_direction = self.current_direction % 8
        return changes

    