import overpy, math

restaurants_ppl_care = { 
    "McDonald's": "GOOD!!!!!", 
    "Burger King": "I'm so sorry.", 
    "Kentucky Fried Chicken": "grease town", 
    "Giraffas": "CORRE",
    "Taco Bell": "🇲🇽💃🌵 ANDALE WEY 🌶️🌮🌯",
}

def ClosestRestaurant(restaurants_found):
    if not restaurants_found:
        return ["Nothing.", "Actual food desert situation. Please seek help"]
    
    for restaurant_name in restaurants_found:
        if restaurant_name in restaurants_ppl_care:
            return [restaurant_name, restaurants_ppl_care[restaurant_name]]
        
    return [restaurants_found[0], "Who cares"]

def CalculateDistance(lat1, lon1, lat2, lon2):
    return math.sqrt((lat1 + lat2)**2 + (lon1 + lon2)**2)

def find_restaurants(lat, lon):
    lat, lon = float(lat), float(lon)
    RADIUS = 15000
    api = overpy.Overpass()

    query = f"""
    [out:json];
    (
      node["amenity"="restaurant"](around:{RADIUS},{lat},{lon});
    );
    out body 25;
    """

    result = api.query(query)
    
    restaurants_found = [
        [node.tags.get("name", "error"), CalculateDistance(lat, lon, float(node.lat), float(node.lon))]
        for node in result.nodes
    ]
    
    return ClosestRestaurant(
        [restaurant_name for restaurant_name, distance in sorted(restaurants_found, key=lambda x:x[1])]
    )