import networkx as nx


excluded_items = [
    ("CONTAINS_FcC", "DOWNREGULATES_CdG", "AFFECTS_CamG", "CONTRAINDICATES_CcD"),
    ("CONTAINS_FcC", "UPREGULATES_CdG", "AFFECTS_CamG", "CONTRAINDICATES_CcD"),
    ("CONTAINS_FcC", "DOWNREGULATES_CdG", "AFFECTS_CamG", "TREATS_CtD"),
    ("CONTAINS_FcC", "UPREGULATES_CdG", "AFFECTS_CamG", "CONTRAINDICATES_CcD"),
    ("CONTAINS_FcC", "UPREGULATES_CdG", "AFFECTS_CamG", "TREATS_CtD"),
    ("CONTAINS_FcC", "DOWNREGULATES_CdG", "UPREGULATES_CuG", "TREATS_CtD"),
    ("CONTAINS_FcC", "DOWNREGULATES_CdG", "UPREGULATES_CuG", "CONTRAINDICATES_CcD"),
    ("CONTAINS_FcC", "UPREGULATES_CuG", "DOWNREGULATES_CdG", "TREATS_CtD"),
    ("CONTAINS_FcC", "UPREGULATES_CuG", "DOWNREGULATES_CdG", "CONTRAINDICATES_CcD"),
    ('CONTAINS_FcC', 'PRODUCES_RpC', 'PARTICIPATES_PpR', 'INCREASEDIN_PiD'),
    ('CONTAINS_FcC', 'AFFECTS_CamG', 'UPREGULATES_CuG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESISTANT_TO_mGrC', 'AFFECTS_CamG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'REDUCES_SEN_mGrsC', 'AFFECTS_CamG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'CONSUMES_RcC', 'PARTICIPATES_GpR', 'ASSOCIATES_DaG'),
    ('CONTAINS_FcC', 'RESISTANT_TO_mGrC', 'UPREGULATES_CuG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'PRODUCES_RpC', 'PARTICIPATES_GpR', 'ASSOCIATES_DaG'),
    ('CONTAINS_FcC', 'AFFECTS_CamG', 'UPREGULATES_CuG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'DOWNREGULATES_CdG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'INTERACTS_PiC', 'BINDS_CbP', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'REDUCES_SEN_mGrsC', 'UPREGULATES_CuG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'CONSUMES_RcC', 'PARTICIPATES_PpR', 'DECREASEDIN_PdD'),
    ('CONTAINS_FcC', 'REDUCES_SEN_mGrsC', 'AFFECTS_CamG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'DOWNREGULATES_CdG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'AFFECTS_CamG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'AFFECTS_CamG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'REDUCES_SEN_mGrsC', 'UPREGULATES_CuG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'UPREGULATES_CuG', 'AFFECTS_CamG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'TRANSPORTS_PtC', 'BINDS_CbP', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESISTANT_TO_mGrC', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'AFFECTS_CamG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'PRODUCES_RpC', 'PARTICIPATES_PpR', 'DECREASEDIN_PdD'),
    ('CONTAINS_FcC', 'AFFECTS_CamG', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'UPREGULATES_CuG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'AFFECTS_CamG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'UPREGULATES_CuG', 'AFFECTS_CamG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'TRANSPORTS_PtC', 'BINDS_CbP', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'UPREGULATES_CuG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESISTANT_TO_mGrC', 'DOWNREGULATES_CdG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'CONSUMES_RcC', 'PARTICIPATES_PpR', 'INCREASEDIN_PiD'),
    ('CONTAINS_FcC', 'CONSUMES_RcC', 'PARTICIPATES_CpR', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'PRODUCES_RpC', 'PARTICIPATES_CpR', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'AFFECTS_CamG', 'DOWNREGULATES_CdG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'RESPONSE_TO_mGrC', 'UPREGULATES_CuG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'REDUCES_SEN_mGrsC', 'DOWNREGULATES_CdG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'RESISTANT_TO_mGrC', 'AFFECTS_CamG', 'CONTRAINDICATES_CcD'),
    ('CONTAINS_FcC', 'ADVRESPONSE_TO_mGarC', 'UPREGULATES_CuG', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'CONSUMES_RcC', 'PARTICIPATES_CpR', 'TREATS_CtD'),
    ('CONTAINS_FcC', 'PRODUCES_RpC', 'PARTICIPATES_CpR', 'TREATS_CtD')
]

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
    metapaths_refined_2 = []
    for item in metapaths_refined:
        if (len(item) == 4):
            if (item not in excluded_items):
                if item[1] != item[2]:
                    metapaths_refined_2.append(item)
        else:
            metapaths_refined_2.append(item)
    return metapaths_refined_2


def generate_combinations(data, current_combination=[], combinations=[]):
    if len(data) == 0:
        combinations.append(tuple(current_combination))
        return
    for item in data[0]:
        generate_combinations(data[1:], current_combination + [item], combinations)