import requests
import backoff


def backoff_hdlr(details):
    print("Backing off {wait:0.1f} seconds after {tries} tries calling function {target}"
          "with args {args} and kwargs {kwargs}".format(**details))


if __name__ == '__main__':
    @backoff.on_exception(
        backoff.expo,
        requests.exceptions.RequestException,
        max_tries=None,
        on_backoff=backoff_hdlr
    )
    def get_url(url):
        return requests.get(url)

    get_url('https://xxxxxxxxxxxxxxxxxxx.org')
