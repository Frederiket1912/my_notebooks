import requests
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


class BookHandler:

    def __init__(self, url_list):
        self.url_list = url_list

    def download(self, url, filename):
        r = requests.get(url)
        if (r.status_code == 404):
            raise Exception("url not found")
        with open(filename, 'w+') as fd:
            fd.write(r.text)

    def multi_download(self):
        self.files = []
        executor = ThreadPoolExecutor(len(self.url_list))
        for idx, url in enumerate(self.url_list):
            filename = 'book'+str(idx)+'.txt'
            self.files.append(filename)
            executor.submit(self.download(url, filename))

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index > len(self.files) - 1:
            raise StopIteration  # signals "the end"
        result = self.files[self.current_index]
        self.current_index += 1
        return result

    def urllist_generator(self):
        for url in self.url_list:
            yield url

    def avg_vowels(self, text):
        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        with open(text, 'rt') as fd:
            data = fd.read()
            words = data.split()
            count = 0
            for word in words:
                lower = word.lower()
                for i in range(0, len(lower)):
                    if lower[i] in vowels:
                        count += 1
            return {text: count / len(words)}

    def hardest_read(self):
        executor = ProcessPoolExecutor(multiprocessing.cpu_count())
        with ProcessPoolExecutor(multiprocessing.cpu_count()) as ex:
            res = ex.map(self.avg_vowels, self.files)
        result = {k: v for d in res for k, v in d.items()}
        result_sorted = {k: v for k, v in sorted(
            result.items(), key=lambda item: item[1], reverse=True)}
        return next(iter(result_sorted.items()))
