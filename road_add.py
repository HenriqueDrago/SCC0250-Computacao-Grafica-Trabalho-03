import json
import copy

def expand_roads(json_path, n):
    # Load the original scene
    with open(json_path, "r", encoding="utf-8") as f:
        scene = json.load(f)

    # Find the central road to use as our base template
    central_road = None
    for obj in scene:
        if obj.get("name") == "Estrada_Central":
            central_road = obj
            break
            
    if not central_road:
        print("Error: Could not find 'Estrada_Central' in the JSON file.")
        return

    # Create a clean scene
    clean_scene = [central_road]

    # Distance between lanes
    offset_x = 13.0962645 
    base_x = central_road["translacao"][0]

    # Generate n roads on both sides
    for i in range(1, n + 1):
        # Left Road (E - Esquerda)
        left_road = copy.deepcopy(central_road)
        left_road["name"] = f"Estrada_E{i:02d}"  # Creates E01, E02, E03...
        left_road["translacao"][0] = base_x - (offset_x * i)
        clean_scene.append(left_road)
        
        # Right Road (D - Direita)
        right_road = copy.deepcopy(central_road)
        right_road["name"] = f"Estrada_D{i:02d}"  # Creates D01, D02, D03...
        right_road["translacao"][0] = base_x + (offset_x * i)
        clean_scene.append(right_road)

    # Save the expanded scene to a new file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clean_scene, f, indent=4)

# run
expand_roads("storage/road.json", n=20)