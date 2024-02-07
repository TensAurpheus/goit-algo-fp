import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq

def add_edges_h(graph, heap, index, pos, x=0, y=0, layer=1):
    if index >= len(heap):
        return None
    graph.add_node(heap[index], color='skyblue', label=heap[index])  # Використання id та збереження значення вузла
    if 2 * index + 1 < len(heap):
        graph.add_edge(heap[index], heap[2 * index + 1])
        l = x - 1 / 2 ** layer
        pos[heap[2 * index + 1]] = (l, y - 1)
        l = add_edges_h(graph, heap, 2 * index + 1, pos, x=l, y=y - 1, layer=layer + 1)
    if 2 * index + 2 < len(heap):
        graph.add_edge(heap[index], heap[2 * index + 2])
        r = x + 1 / 2 ** layer
        pos[heap[2 * index + 2]] = (r, y - 1)
        r = add_edges_h(graph, heap, 2 * index + 2, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_heap(heap):
    tree = nx.DiGraph()
    pos = {heap[0]: (0, 0)}
    tree = add_edges_h(tree, heap, 0, pos)
    # print(pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == '__main__':
    hp = [1, 3, 8, 6, 4, 7, 5, 2]
    hq.heapify(hp)
    print('Heap: ', hp)
    draw_heap(hp)
