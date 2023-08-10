conda run -n pagerank python metapath_dwpc_analysis_profiling.py ../../dwpc_data/food_nodes.csv Food DOID:11476 Disease identifier '|' ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_profiling.prof >> logs/dwpc_profiling_1.log 2>&1 &
echo "Completed iron definciey anemia Disease"
wait