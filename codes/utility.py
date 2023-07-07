import networkx as nx

def get_all_metapaths_for_node_pair(source, target, G_metagraph, max_length=4):
    metapath_count = 0
    metapath_dict = {}
    for path in nx.all_simple_paths(G_metagraph, source, target, cutoff=max_length):
        metapath_count += 1
        edges = []
        for u, v in zip(path[:-1], path[1:]):
            multiple_maps = []
            for item in G_metagraph[u][v].items():
                multiple_maps.append(item[-1]["relation"])
            edges.append(multiple_maps)    
        metapath_dict[metapath_count] = edges

    metapaths = []
    for key, value in metapath_dict.items():
        combinations = []
        generate_combinations(value, combinations=combinations)
        metapaths.extend(combinations)

    metapaths = list(set(metapaths))

    indices_to_remove = []
    for index, path in enumerate(metapaths):
        for item in path:
            if "MEASURES_CLm" in item or "REGULATES_PrG" in item:
                indices_to_remove.append(index)
                break

    metapaths_refined = [elem for i, elem in enumerate(metapaths) if i not in indices_to_remove]
    return metapaths_refined


def generate_combinations(data, current_combination=[], combinations=[]):
    if len(data) == 0:
        combinations.append(tuple(current_combination))
        return
    for item in data[0]:
        generate_combinations(data[1:], current_combination + [item], combinations)