class Codec:
    def __init__(self):
        self.url_map = {}
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        self.counter += 1
        short_url = "http://tinyurl.com/" + str(self.counter)
        self.url_map[short_url] = longUrl
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.url_map.get(shortUrl, "")