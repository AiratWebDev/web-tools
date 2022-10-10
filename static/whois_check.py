from whois import whois

def whois_check(link):
    whois_obj = whois(link)
    return whois_obj
