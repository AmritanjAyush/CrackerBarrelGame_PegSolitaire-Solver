import networkx as nx
import matplotlib.pyplot as plt

first_id_in_row = lambda row: sum(range(row+1))
graph_colors = {'empty': 'grey', 'filled': 'cyan', 'moving':'orange', 'skipped':'red'}

height = 5
graph = nx.Graph()
graph_labels = {}
positions = {}
for row in range(height+1):
    for col in range(row):
        idx = sum(range(row)) + col
        graph_labels[idx] = str(idx)
        positions[idx] = ((col-(height+row)/2)*5, (height-row)*5)
        graph.add_node(idx)
        if col < row-1:
            graph.add_edge(idx, idx+1, typeof='lateral')
        if row < height:
            graph.add_edge(idx, idx+row, typeof='vertical_fwd')
            graph.add_edge(idx, idx+row+1, typeof='vertical_back')


def generate_winning_graphic(move_list, config, turn = 1):
    from_node, skip_node, to_node = move_list[0]
    config.update({from_node:'moving'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig('Frames/Turn {:02d} - Phase {}'.format(turn, 1))
    plt.clf()
    config.update({from_node:'empty', skip_node:'skipped', to_node:'moving'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig('Frames/Turn {:02d} - Phase {}'.format(turn, 2))
    plt.clf()
    config.update({skip_node:'empty', to_node:'filled'})
    nx.draw(graph, pos=positions, node_color=[graph_colors[config[node]] for node in graph.nodes()])
    plt.savefig('Frames/Turn {:02d} - Phase {}'.format(turn, 3))
    plt.clf()
    print('turn {} done!'.format(turn))
    if len(move_list) > 1:
        generate_winning_graphic(move_list[1:], config, turn+1)