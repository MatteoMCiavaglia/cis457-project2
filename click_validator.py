from urllib.parse import urlparse, urlunparse

class ClickRedirectionValidator:
    def __init__(self, whitelist):
        self.whitelist = whitelist

    def remove_dynamic_part(self, url):
        # Parse the URL
        parsed_url = urlparse(url)

        # Reconstruct the URL with only the domain
        return urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))

    def is_whitelisted(self, url):
        # Check if the domain name is whitelisted
        url_domain = self.remove_dynamic_part(url)
        return any(url_domain == self.remove_dynamic_part(whitelisted_url) for whitelisted_url in self.whitelist)

# Example whitelist
whitelist = [
    "https://www.gvsu.edu/",
    "https://www.nvidia.com/",
    "https://www.michigan.gov/"
]

validator = ClickRedirectionValidator(whitelist)

# Test URLs
test_urls = [
    "https://www.gvsuu.edu/fake-websi/te",
    "https://www.nvidiia.com/832rnc7h/f347ty3owtd",
    "https://www.michigan.gov/--72356huf",
    "https://www.gvsu.edu/real/website",
    "https://www.nvidia.com/dkm4k7ty/s37dtmo3s/8kdt8",
    "https://www.miichigan.gov/49380/6tnfd09/736450dj9"
]

# for url in test_urls:
#     if validator.is_whitelisted(url):
#         print(f"{url} is whitelisted")
#     else:
#         print(f"{url} is not whitelisted")

if __name__ == "__main__":
    while True:
        url_input = input("Enter the URL: ")
        if validator.is_whitelisted(url_input):
            print(f"{url_input} is whitelisted")
        else:
            print(f"{url_input} is not whitelisted")
        if url_input == "exit":
            break