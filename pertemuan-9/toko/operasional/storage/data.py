import os 
import json 

def load_data(path):
    """Membaca file json"""
    if not os.path.exists(path):
        return [] 
    try:
        print(f"Loading data from {path}...")
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []
    
    
def save_data(path, data):
    """Membuat file json"""
    try: 
        folder = os.path.dirname(path)
        if folder: 
            os.makedirs(folder, exist_ok=True)
            
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        return True
    
    except IOError:
        return False
    

save_data("data/produk.json", [{"kode": "p01", "nama": "Indomie Goreng", "harga": 3000, "stok": 10}])