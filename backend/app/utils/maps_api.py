import requests
import urllib.parse

def get_coordinates(location_name: str) -> tuple[float, float]:
    """
    Fetches latitude and longitude using OpenStreetMap Nominatim.
    Requires a custom User-Agent per Nominatim Terms of Service.
    """
    url = f"https://nominatim.openstreetmap.org/search?q={urllib.parse.quote(location_name)}&format=json&limit=1"
    headers = {
        "User-Agent": "CulturalRootsExplorer/1.0 (GVSU-Project)"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200 and len(response.json()) > 0:
            data = response.json()[0]
            return float(data['lat']), float(data['lon'])
    except Exception as e:
        print(f"Geocoding error: {e}")
        
    return None, None

def generate_google_maps_url(query: str) -> str:
    """Generates a Universal Google Maps search URL for frontend iframes or links."""
    encoded_query = urllib.parse.quote(query)
    return f"https://www.google.com/maps/search/?api=1&query={encoded_query}"