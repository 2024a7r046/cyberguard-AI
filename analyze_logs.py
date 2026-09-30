import csv
from collections import Counter, defaultdict
from dns_analyzer import analyze_domain

domains = []

with open("../data/sample_dns_logs.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        domains.append(row["domain"])

counts = Counter(domains)

subdomains = defaultdict(set)

for domain in domains:
    parts = domain.split(".")

    if len(parts) >= 3:
        main_domain = ".".join(parts[-2:])
        subdomain = ".".join(parts[:-2])
        subdomains[main_domain].add(subdomain)

print("\n--- CyberGuard DNS Log Analysis ---")

for domain in domains:
    result = analyze_domain(domain)

    parts = domain.split(".")

    if len(parts) >= 3:
        main_domain = ".".join(parts[-2:])
        unique_count = len(subdomains[main_domain])
    else:
        main_domain = domain
        unique_count = 0

    score = result["risk_score"]
    reasons = result["reasons"]

    # Add points for many unique subdomains
    if unique_count >= 5:
        score += 20
        reasons.append("Many unique subdomains under the same domain")

    # Keep score within 100
    score = min(score, 100)

    if score >= 75:
        risk_level = "CRITICAL"
    elif score >= 50:
        risk_level = "HIGH"
    elif score >= 25:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print("\nDomain:", result["domain"])
    print("Risk Score:", score, "/ 100")
    print("Risk Level:", risk_level)
    print("Request Count:", counts[domain])
    print("Main Domain:", main_domain)
    print("Unique Subdomains:", unique_count)

    print("Reasons:")
    for reason in reasons:
        print("-", reason)