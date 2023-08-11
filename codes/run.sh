conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/food_nodes.csv Food DOID:11476 Disease identifier '|' ../../spoke_35M_data/spoke_metagraph.gpickle ../../dwpc_data/spoke_ncats_version_with_more_food_nodes.gpickle ../../dwpc_data/ dwpc_food_osteoporosis_disease.pickle 80 >> logs/dwpc_food_osteoporosis_disease_scaled_down_spoke_and_metapath_pruned_1.log 2>&1 &
echo "Completed computing DWPC Food-Disease matrix"
wait

# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/food_nodes.csv Food DOID:13724 Disease identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_food_scurvy_disease.pickle 120 >> logs/dwpc_food_scurvy_disease_after_funky_edge_correction_1.log 2>&1 &
# echo "Completed scurvy Disease"
# wait


# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/drugs_phase_4.csv Compound GO:0070997 BiologicalProcess identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_drug_neuron_death_bp.pickle 170 >> logs/dwpc_drug_neuron_death_bp_after_funky_edge_correction_1.log 2>&1 &
# echo "Completed neuron death BiologicalProcess"
# wait


# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/drugs_phase_4.csv Compound GO:0042552 BiologicalProcess identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_drug_myelination_bp.pickle 170 >> logs/dwpc_drug_myelination_bp_after_funky_edge_correction_2.log 2>&1 &
# echo "Completed myelination BiologicalProcess"
# wait

# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/drugs_phase_4.csv Compound GO:0048713 BiologicalProcess identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_drug_oligodendrocyte_differentiation_bp.pickle 170 >> logs/dwpc_drug_oligodendrocyte_differentiation_bp_after_funky_edge_correction_1.log 2>&1 &
# echo "Completed Oligo diff BiologicalProcess"
# wait

# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/drugs_phase_4.csv Compound GO:0043209 CellularComponent identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_drug_myelin_sheath_cc.pickle 170 >> logs/dwpc_drug_myelin_sheath_cc_after_funky_edge_correction_1.log 2>&1 &
# echo "Completed myelin sheath CellularComponent"
# wait

# conda run -n pagerank python metapath_dwpc_analysis.py ../../dwpc_data/drugs_phase_4.csv Compound GO:0019911 MolecularFunction identifier ../../spoke_35M_data/spoke_metagraph.gpickle ../../spoke_35M_data/spoke_35M_compound_pruned_version.gpickle ../../dwpc_data/ dwpc_drug_structural_constituent_of_myelin_sheath_mf.pickle 170 >> logs/dwpc_drug_structural_constituent_of_myelin_sheath_mf_after_funky_edge_correction_1.log 2>&1 &
# echo "Completed struct. consti. of myelin sheath MolecularFunction"
