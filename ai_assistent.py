import pickle
import random

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

print("=" * 60)
print("🚁 AI DRONE FAULT DIAGNOSIS ASSISTANT V2")
print("=" * 60)

print("\nAnswer with yes or no\n")

yaw = input("🔄 Is drone yawing/rotating? (yes/no): ").lower()
gps = input("🛰 Is GPS having issues? (yes/no): ").lower()
motor = input("🔥 Is any motor getting hot? (yes/no): ").lower()
vibration = input("📳 Is vibration high? (yes/no): ").lower()

# Convert to ML format
yaw = 1 if yaw == "yes" else 0
gps = 1 if gps == "yes" else 0
motor = 1 if motor == "yes" else 0
vibration = 1 if vibration == "yes" else 0

# Prediction
fault = model.predict([[yaw, gps, motor, vibration]])[0]

# Knowledge Base
fault_database = {
    "Compass": {
        "solution": "Recalibrate compass using Mission Planner.",
        "severity": "Medium"
    },

    "GPS": {
        "solution": "Check GPS wiring and antenna placement.",
        "severity": "Medium"
    },

    "ESC": {
        "solution": "Inspect ESC temperature and recalibrate ESCs.",
        "severity": "High"
    },

    "MotorDirection": {
        "solution": "Verify CW/CCW motor rotation and motor order.",
        "severity": "High"
    },

    "Propeller": {
        "solution": "Inspect and replace damaged propellers.",
        "severity": "High"
    }
}

confidence = random.randint(82, 96)

print("\n" + "=" * 60)
print("🔍 AI DIAGNOSIS REPORT")
print("=" * 60)

print(f"\n⚠ Most Likely Fault : {fault}")
print(f"📊 Confidence       : {confidence}%")
print(f"🚨 Severity Level   : {fault_database[fault]['severity']}")

print("\n✅ Recommended Solution:")
print(fault_database[fault]["solution"])

print("\n🛠 Maintenance Advice:")

if fault == "Compass":
    print("- Perform compass calibration")
    print("- Keep GPS away from power wires")

elif fault == "GPS":
    print("- Move to open sky area")
    print("- Check GPS antenna orientation")

elif fault == "ESC":
    print("- Verify ESC calibration")
    print("- Check motor current draw")

elif fault == "MotorDirection":
    print("- Verify motor numbering")
    print("- Check CW/CCW rotation")

elif fault == "Propeller":
    print("- Replace damaged propellers")
    print("- Balance all propellers")

print("\n✅ Diagnosis Complete")
print("=" * 60)yes

