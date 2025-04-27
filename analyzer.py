import re

# Fonction de détection de patterns suspects dans les logs
def detect_patterns(log_data):
    suspicious_keywords = ["departure", "location changed", "unknown contact", "encrypted msg", "access denied"]
    matches = []
    
    for line in log_data:
        for keyword in suspicious_keywords:
            if keyword.lower() in line.lower():
                matches.append(line.strip())
    return matches


# Simulation d'un fichier log
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
