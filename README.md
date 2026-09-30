# CyberGuard AI

CyberGuard AI is a DNS security analysis tool that detects suspicious DNS patterns that may indicate DNS tunneling or generated/encoded domain activity.

# Objective

The project analyzes DNS domains and assigns a risk score based on suspicious characteristics such as:

- Domain length
- Subdomain length
- Character entropy
- Number of digits
- Possible generated or encoded data
- Multiple unique subdomains

# How It Works

```text
DNS Domain
    ↓
Domain Feature Analysis
    ↓
Entropy & Pattern Detection
    ↓
Risk Scoring
    ↓
LOW / MEDIUM / HIGH / CRITICAL
    ↓
Reasons for the Risk
## 🚀 Live Demo

[Open CyberGuard AI Prototype](https://2024a7r046-cyberguard-ai-app-ojxch0.streamlit.app)
