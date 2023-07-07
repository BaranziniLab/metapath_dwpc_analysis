import sys
import pandas as pd
import pickle
import numpy as np
import time
from utility import *
import os
import multiprocessing as mp


SOURCE_NODE_FILE = sys.argv[1]
SOURCE_NODETYPE = sys.argv[2]
TARGET_NODE = sys.argv[3]
TARGET_NODETYPE = sys.argv[4]
IDENTIFIER_COLUMN = sys.argv[5]
METAGRAPH_PATH = sys.argv[6]
GRAPH_PATH = sys.argv[7]
SAVE_PATH = sys.argv[8]
SAVE_NAME = sys.argv[9]
NCORES = int(sys.argv[10])

DAMPING_FACTOR = -0.4
MAX_META_PATH_LENGTH = 4



with open(METAGRAPH_PATH, "rb") as f:
    G_metagraph = pickle.load(f)
    
with open(GRAPH_PATH, "rb") as f:
    G = pickle.load(f)
    
extracted_metapaths = get_all_metapaths_for_node_pair(SOURCE_NODETYPE, TARGET_NODETYPE, G_metagraph, MAX_META_PATH_LENGTH)

node_file = pd.read_csv(SOURCE_NODE_FILE)
node_file[IDENTIFIER_COLUMN] = SOURCE_NODETYPE + ":" + node_file[IDENTIFIER_COLUMN]
source_nodes = list(node_file[IDENTIFIER_COLUMN].unique())
# source_nodes = source_nodes[0:50]
target_node = TARGET_NODETYPE + ":" + TARGET_NODE


def main():
    start_time = time.time()
    p = mp.Pool(NCORES)
    out_dict_list = p.map(dwpc_pipeline, source_nodes)
    p.close()
    p.join()
    concatenated_dict = {}
    for dictionary in out_dict_list:
        concatenated_dict.update(dictionary)    
    concatenated_dict["metapaths"] = extracted_metapaths
    with open(os.path.join(SAVE_PATH, SAVE_NAME), "wb") as f:
        pickle.dump(concatenated_dict, f)
    print("{} source nodes completed in {} min".format(len(source_nodes), round((time.time()-start_time)/60, 2)))


# def main():
#     start_time = time.time()
#     dwpc_for_all_source_nodes = []
#     for source_node in source_nodes:
#         dwpc_for_a_source_node = []
#         for metapath_selected in extracted_metapaths:
#             metapath_traced = get_all_paths_corresponding_to_a_metapath(source_node, target_node, metapath_selected)
#             dwpc_for_a_source_node.append(compute_dwpc_for_a_metapath(metapath_traced))
#         dwpc_for_all_source_nodes.append(dwpc_for_a_source_node)

#     dwpc_for_all_source_nodes = np.array(dwpc_for_all_source_nodes)
#     np.save(os.path.join(SAVE_PATH, SAVE_NAME), dwpc_for_all_source_nodes, allow_pickle=False)
#     print("{} source nodes completed in {} min".format(len(source_nodes), round((time.time()-start_time)/60, 2)))


def dwpc_pipeline(source_node):
    out = {}
    dwpc_for_a_source_node = []
    for metapath_selected in extracted_metapaths:
        metapath_traced = get_all_paths_corresponding_to_a_metapath(source_node, target_node, metapath_selected)
        dwpc_for_a_source_node.append(compute_dwpc_for_a_metapath(metapath_traced))
    out[source_node] = dwpc_for_a_source_node
    return out

    

def compute_dwpc_for_a_metapath(metapath_traced):
    if len(metapath_traced) != 0:
        pdp_for_all_instances_of_current_metapath = []
        for metapath_instance in metapath_traced:
            path_degree_list = []
            for edge in metapath_instance:
                source_degree_damped = get_degree_of_node_based_on_edgetype(edge[0], edge[1])**DAMPING_FACTOR
                target_degree_damped = get_degree_of_node_based_on_edgetype(edge[-1], edge[1])**DAMPING_FACTOR
                path_degree_list.extend([source_degree_damped, target_degree_damped])
            pdp_for_all_instances_of_current_metapath.append(np.prod(path_degree_list))
        dwpc_of_current_metapath = np.sum(pdp_for_all_instances_of_current_metapath)
    else:
        dwpc_of_current_metapath = 0
    return dwpc_of_current_metapath


def get_degree_of_node_based_on_edgetype(node, edgetype):
    count = 0
    for _, v, data in G.edges(node, data=True):
        if data["edgetype"] == edgetype:
            count += 1
    return count


def get_all_paths_corresponding_to_a_metapath(source_node, target_node, metapath):
    number_of_hops_in_metapath = len(metapath)
    path_traced = []
    if G.has_node(source_node):
        if number_of_hops_in_metapath == 1:
            for neighbor in G.neighbors(source_node):
                if neighbor == target_node and G[source_node][neighbor]["edgetype"] == metapath[0]:
                    path_traced.append((source_node, G[source_node][neighbor]["edgetype"], neighbor))

        elif number_of_hops_in_metapath == 2:
            for neighbor1 in G.neighbors(source_node):
                if G[source_node][neighbor1]["edgetype"] == metapath[0]:
                    for neighbor2 in G.neighbors(neighbor1):
                        if neighbor2 == target_node and G[neighbor1][neighbor2]["edgetype"] == metapath[1]:
                            path_traced.append([
                                (source_node, G[source_node][neighbor1]["edgetype"], neighbor1),
                                (neighbor1, G[neighbor1][neighbor2]["edgetype"], neighbor2)
                            ])

        elif number_of_hops_in_metapath == 3:
            for neighbor1 in G.neighbors(source_node):
                if G[source_node][neighbor1]["edgetype"] == metapath[0]:
                    for neighbor2 in G.neighbors(neighbor1):
                        if G[neighbor1][neighbor2]["edgetype"] == metapath[1]:
                            for neighbor3 in G.neighbors(neighbor2):
                                if neighbor3 == target_node and G[neighbor2][neighbor3]["edgetype"] == metapath[2]:
                                    path_traced.append([
                                        (source_node, G[source_node][neighbor1]["edgetype"], neighbor1),
                                        (neighbor1, G[neighbor1][neighbor2]["edgetype"], neighbor2),
                                        (neighbor2, G[neighbor2][neighbor3]["edgetype"], neighbor3)
                                    ])

        elif number_of_hops_in_metapath == 4:
            for neighbor1 in G.neighbors(source_node):
                if G[source_node][neighbor1]["edgetype"] == metapath[0]:
                    for neighbor2 in G.neighbors(neighbor1):
                        if G[neighbor1][neighbor2]["edgetype"] == metapath[1]:
                            for neighbor3 in G.neighbors(neighbor2):
                                if G[neighbor2][neighbor3]["edgetype"] == metapath[2]:
                                    for neighbor4 in G.neighbors(neighbor3):
                                        if neighbor4 == target_node and G[neighbor3][neighbor4]["edgetype"] == metapath[3]:
                                            path_traced.append([
                                                (source_node, G[source_node][neighbor1]["edgetype"], neighbor1),
                                                (neighbor1, G[neighbor1][neighbor2]["edgetype"], neighbor2),
                                                (neighbor2, G[neighbor2][neighbor3]["edgetype"], neighbor3),
                                                (neighbor3, G[neighbor3][neighbor4]["edgetype"], neighbor4)
                                            ])
    return path_traced


if __name__ == "__main__":
    main()
    