import re
import random
import time

# Fonction de détection de patterns suspects
def detect_patterns(log_data):
    suspicious_keywords = ["departure", "location changed", "unknown contact", "encrypted msg", "access denied"]
    matches = []
    
    for line in log_data:
        for keyword in suspicious_keywords:
            if keyword.lower() in line.lower():
                matches.append(line.strip())
    return matches

# Simulation de réponse automatisée à la détection
def trigger_response(detected_events):
    if not detected_events:
        return

    print("\n[!] Corrélation active...")
    time.sleep(1.2)
    print("[✓] Motifs récurrents confirmés.")
    time.sleep(0.8)
    print("→ Protocole de veille silencieuse enclenché.")
    time.sleep(1)
    # Choix d'un code aléatoire pour "mission"
    codes = ["OP-4239", "VEIL-7", "NIGHTLINE", "X-SIGNAL"]
    code = random.choice(codes)
    print(f":: Dossier classé [{code}] mis en observation passive.")
    time.sleep(1)
    print("Aucune alerte publique. Surveillance uniquement.\n")

# Exemple
def load_fake_logs():
    return [
        "2025-04-20 14:23:45 - User logged in",
        "2025-04-20 14:25:02 - Departure from zone 6 detected",
        "2025-04-20 14:27:18 - Encrypted msg intercepted",
        "2025-04-20 14:30:55 - Access denied to restricted file",
        "2025-04-20 14:32:00 - Location changed: Sector 7",
    ]

if __name__ == "__main__":
    logs = load_fake_logs()
    results = detect_patterns(logs)

    print("=== Suspicious activity detected ===")
    for r in results:
        print(f"> {r}")
    
    trigger_response(results)

        
        
        
        
        
        
        
        

        
        


















































































































































































































