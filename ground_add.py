import json
import copy

def generate_grid(json_path, base_name, center_name, offset_x, offset_z, n):
    # Load the original scene
    with open(json_path, "r", encoding="utf-8") as f:
        scene = json.load(f)

    # Find the center piece to use as a template
    center_obj = None
    for obj in scene:
        if obj.get("name") == center_name:
            center_obj = obj
            break
            
    if not center_obj:
        print(f"Error: Could not find '{center_name}' in the JSON.")
        return

    # Creates a clean scene (the center id added later)
    clean_scene = []

    base_x = center_obj["translacao"][0]
    base_z = center_obj["translacao"][2]

    # Generate the 2D Grid
    # range(-n, n + 1) goes from -1 to 1
    for i in range(-n, n + 1):      # Left to Right (X-axis)
        for j in range(-n, n + 1):  # Back to Front (Z-axis)
            
            # Clone the template
            grid_piece = copy.deepcopy(center_obj)
            
            # Name it based on the coordinates, except if it's the center
            if i == 0 and j == 0:
                grid_piece["name"] = center_name
            else:
                grid_piece["name"] = f"{base_name}_X{i}_Z{j}"
            
            # Apply the offsets
            grid_piece["translacao"][0] = base_x + (i * offset_x * center_obj["escala"][0])
            grid_piece["translacao"][2] = base_z + (j * offset_z * center_obj["escala"][2])
            
            # Add scene
            clean_scene.append(grid_piece)

    # Save
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(clean_scene, f, indent=4)

# run
generate_grid(json_path="chao.json", base_name="Chao", center_name="Chao_Central", offset_x=5.0, offset_z=5.0, n=10)