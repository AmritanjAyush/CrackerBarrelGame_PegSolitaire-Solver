
from network_manager import graph, height


def initialize_board_configuration(initial_empty:list):
    initial_config = {}
    for row in range(height+1):
        for col in range(row):
            idx = sum(range(row)) + col
            initial_config[idx] = 'empty' if idx in initial_empty else 'filled'
    return initial_config

def get_empty(configuration):
  return [key for key, val in configuration.items() if val == 'empty']

class Board:
    def __init__(self, config, move = None):
        self.data = config
        self.children = []
        self.move = move

    def get_possibles(self):
        current_config = self.data.copy()
        for empty_node in get_empty(self.data):
            print('assessing empty node {}'.format(empty_node))
            for neighbor in graph.neighbors(empty_node):
                print('\tlooking at neighbor (node {})'.format(neighbor))
                if self.data[neighbor] == 'filled':
                    for second_degree_neighbor in filter(lambda x: x != empty_node, graph.neighbors(neighbor)):
                        if graph.get_edge_data(neighbor, second_degree_neighbor)['typeof'] == graph.get_edge_data(neighbor, empty_node)['typeof'] and self.data[second_degree_neighbor] == 'filled':
                            current_config.update({second_degree_neighbor:'moving'})
                            break
        return current_config

    def generate_children(self):
        for empty_node in get_empty(self.data):
            for neighbor in graph.neighbors(empty_node):
                if self.data[neighbor] == 'filled':
                    for second_degree_neighbor in filter(lambda x: x != empty_node, graph.neighbors(neighbor)):
                        if graph.get_edge_data(neighbor, second_degree_neighbor)['typeof'] ==graph.get_edge_data(neighbor, empty_node)['typeof'] and self.data[second_degree_neighbor] == 'filled':
                            self.make_child({**self.data, **{empty_node:'filled', neighbor:'empty', second_degree_neighbor:'empty'}}, (second_degree_neighbor, neighbor, empty_node))
                            break

    def make_child(self, config, move = None):
        self.children.append(Board(config, move))

    def get_children(self):
        return self.children

    def count_children(self):
        return len(self.children)

    def score(self):
        return sum(range(height+1)) - len(get_empty(self.data))

    def __str__(self):
        return str(self.data)