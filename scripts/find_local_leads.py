#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import os
import time

def fetch_leads():
    queries = [
        "peluqueria Cali Colombia",
        "salon de belleza Cali Colombia",
        "spa Cali Colombia",
        "estetica Cali Colombia"
    ]
    
    headers = {
        "User-Agent": "NailsWithLoveProspector/1.0 (iam@acoolnerd.com)"
    }
    
    unique_leads = {}
    
    print("Starting local business leads search in Cali, Colombia...")
    for q in queries:
        print(f"Querying for '{q}'...")
        encoded_query = urllib.parse.quote(q)
        url = f"https://nominatim.openstreetmap.org/search?q={encoded_query}&format=json&limit=25"
        
        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                if response.status == 200:
                    data = json.loads(response.read().decode('utf-8'))
                    for item in data:
                        osm_id = item.get("osm_id")
                        if osm_id and osm_id not in unique_leads:
                            # Parse short address
                            display_name = item.get("display_name", "")
                            parts = [p.strip() for p in display_name.split(",")]
                            name = item.get("name", "Salón de Belleza")
                            
                            # Build a clean address
                            clean_address = ", ".join(parts[:4]) if len(parts) >= 4 else display_name
                            
                            # Determine neighborhood/zone
                            neighborhood = "Cali"
                            for part in parts:
                                if "Comuna" in part or "Barrio" in part:
                                    neighborhood = part
                                    break
                            
                            category = item.get("type", "beauty").capitalize()
                            if category == "Hairdresser":
                                category = "Peluquería"
                            elif category == "Spa":
                                category = "Spa"
                            else:
                                category = "Salón de Estética"
                                
                            unique_leads[osm_id] = {
                                "osm_id": osm_id,
                                "name": name,
                                "address": clean_address,
                                "neighborhood": neighborhood,
                                "lat": item.get("lat"),
                                "lon": item.get("lon"),
                                "category": category,
                                "status": "Pendiente",  # Default status for CRM outreach
                                "notes": ""
                            }
                time.sleep(1.2)  # Respect Nominatim's usage policy (1 request/sec max)
        except Exception as e:
            print(f"Error querying '{q}': {e}")
            time.sleep(1)
            
    leads_list = list(unique_leads.values())
    print(f"Search complete. Found {len(leads_list)} unique leads.")
    
    # Save directory setup
    target_dir = "/Users/ACoolNERD/Documents/NAILS with Love by YESENIA/launch-system-9.7/website/dashboard/data"
    os.makedirs(target_dir, exist_ok=True)
    
    output_path = os.path.join(target_dir, "leads.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(leads_list, f, ensure_ascii=False, indent=2)
        
    print(f"Leads data successfully saved to: {output_path}")

if __name__ == "__main__":
    fetch_leads()
