from whoisapi import get_whois

def test_getwhois():
    assert get_whois("google.com") == "google.com"

