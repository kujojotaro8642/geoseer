from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

KONKAN_SITES = [
    {"id": "E1", "zone": "Northern", "lat": 17.047, "lng": 73.256, "score": 88,
     "desc": "V-shaped drainage valley — river meets coast — dual wall rock exposure — sediment concentration zone",
     "methods": ["Visual Analysis", "DEM Elevation", "Boundary Mapping", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E2", "zone": "Northern", "lat": 17.047, "lng": 73.256, "score": 91,
     "desc": "Lithological boundary — orange lateritic to dark basalt transition — fossil concentration at rock interfaces",
     "methods": ["Visual Analysis", "DEM Elevation", "Boundary Mapping", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E3", "zone": "Northern", "lat": 17.047, "lng": 73.256, "score": 87,
     "desc": "Curved cliff embayment — wave cut feature — soft rock preferential erosion — zero vegetation confirmed by NDVI",
     "methods": ["Visual Analysis", "Boundary Mapping", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E4", "zone": "N-Middle", "lat": 17.040, "lng": 73.254, "score": 85,
     "desc": "Vegetation-rock boundary with drainage channel — moisture anomaly — active erosion through platform",
     "methods": ["Visual Analysis", "DEM Elevation", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E5", "zone": "Middle", "lat": 17.035, "lng": 73.252, "score": 86,
     "desc": "Maximum bare rock in middle zone — direct wave action on fresh basalt — lowest middle section NDVI",
     "methods": ["Visual Analysis", "DEM Elevation", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E6", "zone": "Southern", "lat": 17.025, "lng": 73.248, "score": 89,
     "desc": "Flat intertidal platform — multi-directional wave action — visible layering — consistent with 2020 trackway geology",
     "methods": ["Visual Analysis", "Boundary Mapping", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
    {"id": "E7", "zone": "S. Tip", "lat": 17.021, "lng": 73.246, "score": 95,
     "desc": "Peninsula tip — double erosion zone — ALL 5 methods converge — lowest NDVI — maximum elevation drop — highest overall priority",
     "methods": ["Visual Analysis", "DEM Elevation", "Boundary Mapping", "NDVI", "Excavation Analysis"],
     "priority": "CRITICAL"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/research")
def research():
    return render_template("research.html", sites=KONKAN_SITES)

@app.route("/api/sites")
def api_sites():
    return jsonify(KONKAN_SITES)

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.json
    region = data.get("region", "Unknown")
    import random
    scores = {
        "dem_terrain": random.randint(55, 90),
        "coastal_proximity": random.randint(50, 92),
        "ndvi_pattern": random.randint(48, 88),
        "slope_aspect": random.randint(45, 85),
        "geology_match": random.randint(50, 90),
        "site_density": random.randint(40, 80),
    }
    overall = sum(scores.values()) // len(scores)
    return jsonify({
        "region": region,
        "overall_score": overall,
        "layer_scores": scores,
        "priority": "CRITICAL" if overall > 80 else "HIGH" if overall > 65 else "MODERATE",
        "note": "Demo analysis. Full model uses real satellite data ingestion."
    })

if __name__ == "__main__":
    app.run(debug=True)
