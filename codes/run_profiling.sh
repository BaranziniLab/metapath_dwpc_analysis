conda run -n pagerank python metapath_dwpc_analysis_profiling.py ../../dwpc_data/food_nodes.csv Food DOID:11476 Disease identifier ':' ../../spoke_35M_data/spoke_metagraph.gpickle ../../dwpc_data/spoke_850T.gpickle ../../dwpc_data/ dwpc_profiling_using_spoke850T.prof >> logs/dwpc_profiling_4.log 2>&1 &
echo "Completed profiling"
wait