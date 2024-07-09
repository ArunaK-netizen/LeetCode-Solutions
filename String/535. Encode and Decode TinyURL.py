class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        encodedURL = ""
        for i in longUrl:
            encodedURL += chr(ord(i) + 1)
        return encodedURL

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decodedUrl = ""
        for i in shortUrl:
            decodedUrl += chr(ord(i) - 1)
        return decodedUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))