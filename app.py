import os
import joblib
import pandas as pd
from flask import Flask, render_template, request

# -----------------------------------------------------------------------------
# EXPLICIT TEMPLATE FOLDER PATH FIX
# -----------------------------------------------------------------------------
# This guarantees Flask finds 'templates/index.html' regardless of where you run python app.py from
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# Load model and feature metadata relative to app.py
MODEL_PATH = os.path.join(BASE_DIR, "asteroid_model.pkl")
FEATURES_PATH = os.path.join(BASE_DIR, "model_features.pkl")

model = joblib.load(MODEL_PATH)
feature_cols = joblib.load(FEATURES_PATH)


@app.route("/", methods=["GET", "POST"])
def home():
    prediction_text = None
    threat_status = None

    if request.method == "POST":
        try:
            abs_mag = float(request.form["absolute_magnitude"])
            est_diam_min = float(request.form["estimated_diameter_min"])
            est_diam_max = float(request.form["estimated_diameter_max"])
            velocity = float(request.form["relative_velocity"])
            miss_dist = float(request.form["miss_distance"])
            moid = float(request.form["min_orbit_intersection"])

            # Feature Engineering matching training pipeline
            est_diam_avg = (est_diam_min + est_diam_max) / 2.0
            diameter_range = est_diam_max - est_diam_min
            kinetic_energy = (est_diam_avg**3) * (velocity**2)
            pha_flag = 1 if (abs_mag <= 22.0 and moid <= 0.05) else 0

            input_data = {
                "absolute_magnitude": abs_mag,
                "estimated_diameter_min": est_diam_min,
                "estimated_diameter_max": est_diam_max,
                "relative_velocity": velocity,
                "miss_distance": miss_dist,
                "minimum_orbit_intersection": moid,
                "estimated_diameter_avg": est_diam_avg,
                "diameter_range": diameter_range,
                "kinetic_energy_proxy": kinetic_energy,
                "pha_threshold_flag": pha_flag,
            }

            input_df = pd.DataFrame([input_data]).reindex(
                columns=feature_cols, fill_value=0
            )
            pred = model.predict(input_df)[0]
            prob = model.predict_proba(input_df)[0][1] * 100

            if pred == 1:
                threat_status = "HAZARDOUS"
                prediction_text = f"⚠️ THREAT DETECTED! Potentially Hazardous Asteroid (Confidence: {prob:.2f}%)"
            else:
                threat_status = "SAFE"
                prediction_text = f"✅ SAFE OBJECT. Non-Hazardous Asteroid (Hazard Probability: {prob:.2f}%)"

        except Exception as e:
            prediction_text = f"Error processing prediction: {str(e)}"

    return render_template(
        "index.html",
        prediction_text=prediction_text,
        threat_status=threat_status,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)