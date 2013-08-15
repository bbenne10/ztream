import urllib.request
import urllib.parse
from json import loads

LINKS = []
BASE_URL = 'http://gdata.youtube.com/feeds/api/videos?'
AUTHOR = 'majesticcasual'


def parse_links(resp):
    _links = []
    try:
        for entry in resp['feed']['entry']:
            for link in entry['link']:
                if link['type'] == 'text/html' and link['rel'] == 'alternate':
                    _links.append(link['href'].rstrip('&feature=youtube_gdata'))
        return _links
    except KeyError:
        return []


if __name__ == '__main__':
    options = {}
    options['max-results'] = '50'
    options['alt'] = 'json'
    options['author'] = AUTHOR

    i = 1
    total = 2

    while i < total:
        options['start-index'] = i
        query_string = urllib.parse.urlencode(options)
        url = BASE_URL + query_string

        raw = urllib.request.urlopen(url)
        resp = loads(raw.read().decode('utf-8'))
        to_ext = parse_links(resp)
        if not to_ext:
            break
        LINKS.extend(to_ext)
        if total == 2:
            total = resp['feed']['openSearch$totalResults']['$t']
            print("TOTAL: {}".format(total))
        i = len(LINKS)
    with open(AUTHOR, 'w') as f:
        for link in LINKS:
            f.write(str(link) + '\n')
