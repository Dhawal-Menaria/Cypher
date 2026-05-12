import json
import openai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

CYPHER_PROMPT = """
You are Cypher, an AI cybersecurity assistant.
You help developers, students, and IT professionals understand:

- Common vulnerabilities (XSS, SQLi, CSRF, SSRF, Buffer Overflow, etc.)
- Security best practices for web apps and APIs
- How to read and understand CVEs
- Basics of penetration testing concepts (educational only)
- Network security fundamentals
- Tools like Nmap, Burp Suite, Wireshark (educational use only)
- Cryptography concepts (AES, RSA, hashing, etc.)
- OWASP Top 10
- Cloud security basics (AWS, GCP misconfigurations)
- Secure coding practices

Rules:
- NEVER provide working exploit code or help attack real systems
- Always clarify if something is for educational or CTF use only
- Be concise, technical but approachable
- If asked something dangerous or illegal, firmly decline
- Reference OWASP, NIST, or CVE databases when relevant
- Format responses clearly — use short paragraphs or bullet points

You are a learning assistant, not a hacking tool.
"""

def home(request):
    threats = [
        {
            'source': 'The Hacker News',
            'time_ago': '10m ago',
            'badge_type': 'BREACH',
            'badge_classes': 'bg-error/20 text-error border border-error/30',
            'title': 'Major Telco Confirms Data Exfiltration Impacting 10M Users',
            'read_more': '#'
        },
        {
            'source': 'CVE Database',
            'time_ago': '45m ago',
            'badge_type': 'VULNERABILITY',
            'badge_classes': 'bg-tertiary-container/20 text-tertiary-container border border-tertiary-container/30',
            'title': 'Critical RCE (CVE-2025-1042) Discovered in Popular CI/CD Pipeline',
            'read_more': '#'
        },
        {
            'source': 'BleepingComputer',
            'time_ago': '1h ago',
            'badge_type': 'MALWARE',
            'badge_classes': 'bg-secondary-container/20 text-secondary-container border border-secondary-container/30',
            'title': "New Ransomware Strain 'Crypta' Targeting Healthcare Sector",
            'read_more': '#'
        },
        {
            'source': 'CISA Alerts',
            'time_ago': '2h ago',
            'badge_type': 'VULNERABILITY',
            'badge_classes': 'bg-tertiary-container/20 text-tertiary-container border border-tertiary-container/30',
            'title': 'Active Exploitation of Zero-Day in Enterprise VPN Gateways',
            'read_more': '#'
        },
        {
            'source': 'Dark Web Intel',
            'time_ago': '3h ago',
            'badge_type': 'BREACH',
            'badge_classes': 'bg-error/20 text-error border border-error/30',
            'title': '15M Records Dumped on Forum Attributed to Retail Giant',
            'read_more': '#'
        },
        {
            'source': 'CyberNews',
            'time_ago': '4h ago',
            'badge_type': 'MALWARE',
            'badge_classes': 'bg-secondary-container/20 text-secondary-container border border-secondary-container/30',
            'title': 'InfoStealer Campaign Using Fake Software Updates Spreading Rapidly',
            'read_more': '#'
        },
    ]
    return render(request, 'index.html', {'threats': threats})


@csrf_exempt
def chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
        history = data.get('history', [])

        if not user_message:
            return JsonResponse({'error': 'Empty message'}, status=400)

        messages = [{"role": "system", "content": CYPHER_PROMPT}]

        for msg in history[-10:]:
            messages.append({"role": msg['role'], "content": msg['content']})

        messages.append({"role": "user", "content": user_message})

        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=400,
            temperature=0.7,
        )

        return JsonResponse({
            'reply': response.choices[0].message.content,
            'status': 'ok'
        })

    except openai.AuthenticationError:
        return JsonResponse({'error': 'Invalid API key'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)