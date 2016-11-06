from urllib.parse import urlparse


# Get domain name (example.com)
def get_domain(url):
    try:
        link = get_sub_domain(url).split('.')
        return link[-2] + '.' + link[-1]
    except Exception as e:
        print(str(e))
        return ''


# Get sub domain name (name.example.com)
def get_sub_domain(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
        print(str(e))
        return ''
