# Planetary_defence_system
Asteroid Threat Predictor An AI-powered web app that analyzes Near-Earth Asteroids using NASA data and predicts if they are Potentially Hazardous to Earth.
1. What This Project Does
   NASA considers an asteroid Potentially Hazardous if it meets two key rules:
 Size: It is large enough to survive atmospheric entry ($140\text{ meters}$ or wider / Absolute Magnitude $H \le 22.0$).
 Distance: Its orbit brings it close to Earth ($\text{MOID} \le 0.05\text{ AU}$ or ~7.5 million km).
 This project uses Machine Learning to look at asteroid measurement data and predict if an asteroid poses a threat.

Model Performance
We trained and tuned a Random Forest machine learning model to detect hazardous asteroids.
Accuracy: 99.5%Recall (Catching Threats): 92.0% (High recall ensures we almost never miss a dangerous asteroid)ROC-AUC Score: 0.998

Practical Uses
Early Warning: Quickly flags dangerous asteroids from massive astronomy datasets.Triage for Space Telescopes: Helps astronomers prioritize which objects need immediate follow-up tracking.Deflection Mission SupportGives fast impact threat risk estimates for planetary defense teams.
Future Improvements
Space Weather & Solar Effects:Account for solar radiation pressure pushing small asteroids off course over time.Deep Learning:Train AI directly on raw telescope brightness images.Cloud Deployment: Package the app into Docker to run on cloud platforms like Render or AWS.
