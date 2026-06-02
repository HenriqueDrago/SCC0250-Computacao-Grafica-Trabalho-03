import os, json

def remove_entries(file_paths, entries_to_remove):
    scene = None

    for fp in file_paths:
        with open(fp, "r", encoding="utf-8") as f:
            scene = json.load(f)
    
        for obj in scene:
            for entry in entries_to_remove:
                obj.pop(entry, None)
            
            # obj["direction"] = [0.0, -1.0, 0.0]
            # obj["cutoff"] = -1.1
            obj["intensity"] = 1.0
        
                
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(scene, f, indent=4)


remove_entries(["storage/light.json"], [])
    