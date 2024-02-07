import uuid

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, algo):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    plt.title(algo)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def dfs(node, color, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    node.color = color
    color = color_change(color)
    if node.left not in visited and node.left:
        color = dfs(node.left, color, visited)
    if node.right not in visited and node.right:
        color = dfs(node.right, color, visited)
    return color
    

def bfs(root, color):
    if root is None:
        return result
    
    queue = [root]
    while queue:
        level_values = []
        next_level = []
        for node in queue:
            node.color = color
            color = color_change(color)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
    

def color_change(old_rgb):
    new_rgb = tuple(round(256 - (256 - int(old_rgb[i:i+2], 16)) / 1.25) for i in (1, 3, 5))
    # print(new_rgb)
    return f'#{new_rgb[0]:02x}{new_rgb[1]:02x}{new_rgb[2]:02x}'


if __name__ == '__main__':
# Створення дерева
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    color = '#020224'

    dfs(root, color)
    draw_tree(root, 'DFS')
    bfs(root, color)
    draw_tree(root, 'BFS')