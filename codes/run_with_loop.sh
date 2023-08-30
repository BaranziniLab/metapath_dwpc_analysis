
SOURCE_NODE_FILE="../../dwpc_data/food_nodes.csv"
SOURCE_NODE_TYPE="Food"
TARGET_NODE_TYPE="Disease"
IDENTIFIER_COLUMN="identifier"
NODETYPE_SEPARATOR=":"
METAGRAPH_PATH="../../spoke_35M_data/spoke_metagraph.gpickle"
GRAPH_PATH="../../dwpc_data/spoke_850T.gpickle"
SAVE_PATH="../../dwpc_data/"
NCORES=80

DISEASE_IDS=("DOID:10609" "DOID:13725" "DOID:8457" "DOID:12176" "DOID:8499" "DOID:10573" "DOID:13579" "DOID:12328" "DOID:8454" "DOID:10138" "DOID:11249" "DOID:0050810" "DOID:14026" "DOID:13381" "DOID:8455" "DOID:4500" "DOID:0050336")
DISEASE_NAMES=("rickets" "beriberi" "pellagra" "goiter" "night_blindness" "osteomalacia" "kwashiorkor" "marasmus" " riboflavin_deficiency" "xerophthalmia" "vitamin_K_deficiency_bleeding" "biotin_deficiency" "folic_acid_deficiency_anemia" "pernicious_anemia" "pyridoxine_deficiency_anemia" "hypokalemia" "hypophosphatemia")

for i in "${!DISEASE_IDS[@]}"; do
    DISEASE_ID="${DISEASE_IDS[$i]}"
    DISEASE_NAME="${DISEASE_NAMES[$i]}"
    
    conda run -n pagerank python metapath_dwpc_analysis.py "$SOURCE_NODE_FILE" "$SOURCE_NODE_TYPE" "$DISEASE_ID" "$TARGET_NODE_TYPE" "$IDENTIFIER_COLUMN" "$NODETYPE_SEPARATOR" "$METAGRAPH_PATH" "$GRAPH_PATH" "$SAVE_PATH" "dwpc_food_${DISEASE_NAME}_disease.pickle" "$NCORES" >> "logs/dwpc_food_${DISEASE_NAME}_spoke_850T_1.log" 2>&1 &
    wait
    echo "Completed computing DWPC Food-Disease matrix for $DISEASE_NAME"
    
done
