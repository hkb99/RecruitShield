import re
import requests
import dns.resolver
import ipaddress
import tldextract

def get_domain(email):
    email = email.strip()

    domain = email.rsplit("@", 1)[1].lower().rstrip(".")

    extracted = tldextract.extract (
        domain,
        include_psl_private_domains=False
    )

    if not extracted.domain or not extracted.suffix:
        raise ValueError("Invalid domain")

    return domain

def get_dns(domain):

    resolver = dns.resolver.Resolver()
    resolver.timeout = 2
    resolver.lifetime = 4

    results = {}

    for record_type in ("MX", "A", "AAAA"):
        try:
            answers = resolver.resolve(domain, record_type)
            results[record_type] = [str(answer).strip() for answer in answers][:10]
        except dns.exception.DNSException:
            results[record_type] = []


    return results


def analyze_email(email):
    domain = get_domain(email)
    return {
        "email_domain": domain,
        "dns": get_dns(domain),
        "rdap": {"rdap feature no implemented yet"}
    }
