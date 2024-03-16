import requests
import networkx as nx
import pandas as pd



END_POINT = "/api/v1/metagraph"

def get_api_resp(END_POINT, params=None):
    URI = BASE_URI + END_POINT
    if params:
        return requests.get(URI, params=params)
    else:
        return requests.get(URI)



def get_metagraph(spoke_instance='prod'):
    global BASE_URI
    if spoke_instance=='prod':
        BASE_URI = "https://spoke.rbvi.ucsf.edu"
    else:
        BASE_URI = "https://spokedev.rbvi.ucsf.edu"    
    result = get_api_resp(END_POINT)
    data_spoke_metagraph = result.json()
    nodetype_list = []
    for item in data_spoke_metagraph:
        if "source" not in item["data"].keys():
            nodetype_list.append((item["data"]["id"], item["data"]["name"]))
    nodetype_df = pd.DataFrame(nodetype_list, columns=["node_id", "node_name"])
    edgetype_list = []
    for item in data_spoke_metagraph:
        if "source" in item["data"].keys():
            source_name = nodetype_df[nodetype_df["node_id"] == item["data"]["source"]]["node_name"].values[0]
            target_name = nodetype_df[nodetype_df["node_id"] == item["data"]["target"]]["node_name"].values[0]
            edgetype_name = item["data"]["name"]
            edgetype_list.append((source_name, edgetype_name, target_name))

    edgetype_df = pd.DataFrame(edgetype_list, columns=["source", "edgetype", "target"])
    edgetype_df.drop_duplicates(inplace=True)
    edgetype_df_no_self_loops = edgetype_df[~(edgetype_df["source"] == edgetype_df["target"])]
    edgetype_df_self_loops = edgetype_df[edgetype_df["source"] == edgetype_df["target"]]
    edgetype_df_self_loops.target = edgetype_df_self_loops.target.apply(lambda x:x+"_2")
    edgetype_df_extra = pd.merge(edgetype_df_no_self_loops, edgetype_df_self_loops, on="source").drop(["source", "edgetype_y"], axis=1).rename(columns={"target_y":"source", "target_x":"target", "edgetype_x":"edgetype"})[["source", "target", "edgetype"]]
    edgetype_df_extra.drop_duplicates(inplace=True)

    G_metagraph = nx.MultiGraph()
    for index, row in edgetype_df_no_self_loops.iterrows():
        G_metagraph.add_node(row['source'])
        G_metagraph.add_node(row['target'])
        G_metagraph.add_edge(row['source'], row['target'], relation=row["edgetype"])

    for index, row in edgetype_df_self_loops.iterrows():
        G_metagraph.add_node(row['target'])
        G_metagraph.add_edge(row['source'], row['target'], relation=row["edgetype"])

    for index, row in edgetype_df_extra.iterrows():
        G_metagraph.add_edge(row['source'], row['target'], relation=row["edgetype"])
    return G_metagraph
    



