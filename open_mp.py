"""
Author: Chukwunazaekpere Emmanuel Obioma
Lecture: Sorting
Nationality: Biafran
Email-1: chukwunazaekpere.obioma@ue-germany.de 
Email-2: ceo.naza.tech@gmail.com
************************************************
Implementation: to implement the sequential implementation of DFS
Course: Multi-core Programming
Written: Nov 26th 2024
Due: Nov 30th 2024
"""

from omp4py import *
from datetime import datetime
import logging
from time import time
logger = logging.getLogger(__name__)
log_date = datetime.now()
logging.basicConfig(level=logging.INFO)


@omp # decoraor signifying OMP4Py directive
def dfs_sequential(tree:dict, node:str, nodes_visited=None):
    if nodes_visited is None:
        nodes_visited = set()  # set is a non-hierarchical python data type, which does not permit repetitions
    nodes_visited.add(node)    # the root node is added into the nodes_visited nodes
    # print("\n\t node: ", node)         
    with omp("for"):
        for child in range(len(tree[node])):  # Recursively implemetation for visiting un-nodes_visited nodes
            child_nodes = tree[node]
            if child_nodes[child] not in nodes_visited:
                dfs_sequential(tree, child_nodes[child], nodes_visited)

    return nodes_visited

# Run DFS starting from root node 'A'
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [], 'I': [], 'J': [], 'K': [],
    'L': [], 'M': [], 'N': [], 'O': []
}
if __name__ == "__main__":
    start_time = time()
    nodes_visited = dfs_sequential(tree, 'A')
    print("\n\t nodes_visited: ", nodes_visited)
    logging.info(msg=f"\n\t total time taken: {(time()-start_time)} secs")