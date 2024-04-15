import re

class ClickRedirectionValidator:
    def __init__(self, whitelist):
        self.whitelist = whitelist

    def remove_dynamic_part(self, url):
        # Remove dynamic parts of the URL after the domain name
        # For example, convert https://example.com/page?param=value to https://example.com/
        return re.sub(r'://[^/]+/', '://', url)

    def is_whitelisted(self, url):
        # Check if the domain name is whitelisted
        url_domain = self.remove_dynamic_part(url)
        return any(url_domain == self.remove_dynamic_part(whitelisted_url) for whitelisted_url in self.whitelist)

# Example usage
whitelist = [
    "https://www.gvsuu.edu/fake-websi/te",
    "https://www.nvidiia.com/832rnc7h/f347ty3owtd",
    "https://www.michigan.gov/--72356huf",
    "https://www.gvsu.edu/real/website",
    "https://www.nvidia.com/dkm4k7ty/s37dtmo3s/8kdt8",
    "https://www.miichigan.gov/49380/6tnfd09/736450dj9"
]

validator = ClickRedirectionValidator(whitelist)

# Test URLs
test_urls = [
    "https://www.gvsu.edu/",
    "https://www.nvidia.com/",
    "https://www.michigan.gov/"
]

for url in test_urls:
    if validator.is_whitelisted(url):
        print(f"{url} is whitelisted")
    else:
        print(f"{url} is not whitelisted")