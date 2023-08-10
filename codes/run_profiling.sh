conda run -n pagerank python metapath_dwpc_analysis_profiling.py ../../dwpc_data/food_nodes.csv Food DOID:11476 Disease identifier '|' ../../spoke_35M_data/spoke_metagraph.gpickle ../../ncats/data/spoke_graph_ncats_version_2021_02_07.gpickle ../../dwpc_data/ dwpc_profiling_using_scaled_down_spoke.prof >> logs/dwpc_profiling_2.log 2>&1 &
echo "Completed profiling"
wait