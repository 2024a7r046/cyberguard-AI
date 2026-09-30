import math
from collections import Counter


def calculate_entropy(text):
    if not text:
        return 0

    counts = Counter(text)
    length = len(text)

    entropy = 0
    for count in counts.values():
        probability = count / length
        entropy -= probability * math.log2(probability)

    return entropy


def analyze_domain(domain):
    domain = domain.lower().strip()

    score = 0
    reasons = []

    parts = domain.split(".")
    longest_part = max(parts, key=len)

    if len(domain) > 50:
        score += 20
        reasons.append("Unusually long domain")

    if len(longest_part) > 30:
        score += 20
        reasons.append("Very long subdomain")

    entropy = calculate_entropy(longest_part)

    if entropy > 3.5:
        score += 20
        reasons.append("High entropy or randomness")

    digit_count = sum(char.isdigit() for char in longest_part)

    if digit_count >= 5:
        score += 15
        reasons.append("Large number of digits")

    if len(longest_part) > 20 and digit_count >= 3:
        score += 15
        reasons.append("Possible encoded or generated data")

    score = min(score, 100)

    if score >= 80:
        risk_level = "CRITICAL"
    elif score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "domain": domain,
        "entropy": round(entropy, 2),
        "risk_score": score,
        "risk_level": risk_level,
        "reasons": reasons
    }


if __name__ == "__main__":
    domain = input("Enter DNS domain: ")

    result = analyze_domain(domain)

    print("\n--- CyberGuard DNS Analysis ---")
    print("Domain:", result["domain"])
    print("Entropy:", result["entropy"])
    print("Risk Score:", result["risk_score"], "/ 100")
    print("Risk Level:", result["risk_level"])

    print("\nReasons:")

    if result["reasons"]:
        for reason in result["reasons"]:
            print("-", reason)
    else:
        print("- No major suspicious indicators found")