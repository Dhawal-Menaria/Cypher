from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # Threat data array
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
            'title': 'New Ransomware Strain \'Crypta\' Targeting Healthcare Sector',
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
        {
            'source': 'CyberNews',
            'time_ago': '4h ago',
            'badge_type': 'MALWARE',
            'badge_classes': 'bg-secondary-container/20 text-secondary-container border border-secondary-container/30',
            'title': 'InfoStealer Campaign Using Fake Software Updates Spreading Rapidly',
            'read_more': '#'
        }
    ]
    
    context = {
        'threats': threats
    }
    
    return render(request, 'index.html', context)