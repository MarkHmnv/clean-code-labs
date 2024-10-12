from abc import ABC, abstractmethod


# 1. Interface Definition
class Downloader(ABC):
    @abstractmethod
    def download(self, url: str) -> str:
        """Download data from the given URL."""
        ...


# 2. Concrete Implementation
class SimpleDownloader(Downloader):
    def download(self, url: str) -> str:
        """Simulate downloading data."""
        print(f'Downloading from {url}...')
        return f'Data from {url}'


# 3. Proxy Implementation with Caching
class CachingDownloader(Downloader):
    def __init__(self, downloader: Downloader):
        self.downloader = downloader
        self.cache = {}

    def download(self, url: str) -> str:
        if url in self.cache:
            print(f'Returning cached data for {url}.')
            return self.cache[url]

        print(f'Cache miss for {url}. Downloading...')
        data = self.downloader.download(url)
        self.cache[url] = data
        return data


# 4. Client Code Example
def client_code(downloader: Downloader, url: str):
    print(downloader.download(url))
    print(downloader.download(url))


if __name__ == '__main__':
    url = 'http://example.com/resource'

    print('Using SimpleDownloader:')
    simple_downloader = SimpleDownloader()
    client_code(simple_downloader, url)

    print('\nUsing CachingDownloader:')
    caching_downloader = CachingDownloader(simple_downloader)
    client_code(caching_downloader, url)
