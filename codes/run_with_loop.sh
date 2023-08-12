
SOURCE_NODE_FILE="../../dwpc_data/food_nodes.csv"
SOURCE_NODE_TYPE="Food"
TARGET_NODE_TYPE="Disease"
IDENTIFIER_COLUMN="identifier"
NODETYPE_SEPARATOR=":"
METAGRAPH_PATH="../../spoke_35M_data/spoke_metagraph.gpickle"
GRAPH_PATH="../../dwpc_data/spoke_850T.gpickle"
SAVE_PATH="../../dwpc_data/"
NCORES=80

DISEASE_IDS=("DOID:11476" "DOID:13724" "DOID:11758" "DOID:2355")
DISEASE_NAMES=("osteoporosis" "scurvy" "iron_deficiency_anemia" "anemia")

for i in "${!DISEASE_IDS[@]}"; do
    DISEASE_ID="${DISEASE_IDS[$i]}"
    DISEASE_NAME="${DISEASE_NAMES[$i]}"
    
    conda run -n pagerank python metapath_dwpc_analysis.py "$SOURCE_NODE_FILE" "$SOURCE_NODE_TYPE" "$DISEASE_ID" "$TARGET_NODE_TYPE" "$IDENTIFIER_COLUMN" "$NODETYPE_SEPARATOR" "$METAGRAPH_PATH" "$GRAPH_PATH" "$SAVE_PATH" "dwpc_food_${DISEASE_NAME}_disease.pickle" "$NCORES" >> "logs/dwpc_food_${DISEASE_NAME}_spoke_850T_1.log" 2>&1 &
    wait
    echo "Completed computing DWPC Food-Disease matrix for $DISEASE_NAME"
    
done
