# Planetary_defence_system
Asteroid Threat Predictor An AI-powered web app that analyzes Near-Earth Asteroids using NASA data and predicts if they are Potentially Hazardous to Earth.
1. What This Project Does
   NASA considers an asteroid Potentially Hazardous if it meets two key rules:
 Size: It is large enough to survive atmospheric entry ($140\text{ meters}$ or wider / Absolute Magnitude $H \le 22.0$).
 Distance: Its orbit brings it close to Earth ($\text{MOID} \le 0.05\text{ AU}$ or ~7.5 million km).
 This project uses Machine Learning to look at asteroid measurement data and predict if an asteroid poses a threat.

2.Model Performance
We trained and tuned a Random Forest machine learning model to detect hazardous asteroids.
Accuracy: 99.5%Recall (Catching Threats): 92.0% (High recall ensures we almost never miss a dangerous asteroid)ROC-AUC Score: 0.998

3.Practical Uses
Early Warning: Quickly flags dangerous asteroids from massive astronomy datasets.Triage for Space Telescopes: Helps astronomers prioritize which objects need immediate follow-up tracking.Deflection Mission SupportGives fast impact threat risk estimates for planetary defense teams.
4.Future Improvements
Space Weather & Solar Effects:Account for solar radiation pressure pushing small asteroids off course over time.Deep Learning:Train AI directly on raw telescope brightness images.Cloud Deployment: Package the app into Docker to run on cloud platforms like Render or AWS.


What We Are Looking For ?
When scanning Near-Earth Objects (NEOs), astronomers process thousands of newly discovered space rocks every year. Our project solves a critical problem: How do we instantly identify which asteroids pose an actual threat to Earth without relying solely on manual calculation?
Key Objectives:
 Detect High-Risk Asteroids: We analyze physical and orbital features—such as brightness ($H$), velocity, approach distance, and Minimum Orbit Intersection       
 Distance ($\text{MOID}$)—to determine if an asteroid is a Potentially Hazardous Asteroid (PHA).
 
 Zero Tolerance for Missed Threats (High Recall): In planetary defense, a False Positive (labeling a safe asteroid as hazardous) is just a false alarm, but a False Negative (missing a real threat) could be catastrophic. Our model specifically optimizes for high Recall to ensure no dangerous asteroid slips through undetected.
 
 Real-Time Prediction Interface: Provide a lightweight, web-based tool where researchers or users can input raw asteroid telemetry and receive instant risk classifications with probability confidence scores.


Technologies used in this project
python
scikit-learn
pandas
numpy
flask
joblib
html
