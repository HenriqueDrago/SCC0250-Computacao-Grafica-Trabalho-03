import os, json

def remove_entries(file_paths, entries_to_remove):
    scene = None

    for fp in file_paths:
        with open(fp, "r", encoding="utf-8") as f:
            scene = json.load(f)
    
        for obj in scene:
            for entry in entries_to_remove:
                obj.pop(entry, None)
                obj["illum_specs"] = {
                    "ka": 0.0,
                    "kd": 0.0,
                    "ks": 0.0,
                    "ns": 0.0
                }
        
        with open(fp, "w", encoding="utf-8") as f:
            json.dump(scene, f, indent=4)


remove_entries(["storage/scene.json", "storage/road.json", "storage/chao.json"], ["id_textura", "obj_id", "scene_id", "angulo_obj"])
    