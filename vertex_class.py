#This file contains code defining a vertex class and a function to generate random graphs.


import numpy as np

class vertex:

    def __init__(self,name):
        self.name = name
        self.neighborhood = {}
        self.data = None


    def add_neighbor(self,neighbor):

        self.neighborhood[neighbor.name] = neighbor
        neighbor.neighborhood[self.name] = self



def generate_random_graph(num_vertices = 10):


    vertex_list = []


    for i in range(num_vertices):
        vertex_list.append(vertex(i))

    edges = np.zeros((num_vertices,num_vertices))



    for i in range(num_vertices):

        j = 0

        while j < i:

            edge_coef = np.random.randint(2)

            
            if edge_coef == 1:

                vertex_list[i].add_neighbor(vertex_list[j])

                edges[i,j] = 1
            
            j+=1



    edges = ((edges + edges.T) > 0).astype(int)

    graph = {}
    graph['v'] = vertex_list
    graph['e'] = edges

    return graph

