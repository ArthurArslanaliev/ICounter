import urlparse


class UrlUtils(object):
    @staticmethod
    def is_relative(uri):
        parts = urlparse.urlparse(UrlUtils.escape(uri))
        return not parts[1]

    @staticmethod
    def is_internal(base_uri, uri):
        escaped = UrlUtils.escape(uri)
        if escaped.startswith(base_uri):
            return True
        parts = urlparse.urlparse(escaped)
        if not parts[0] and not parts[1]:
            return True
        return False

    @staticmethod
    def to_absolute(base_uri, uri):
        return urlparse.urljoin(base_uri, uri)

    @staticmethod
    def escape(uri):
        if isinstance(uri, unicode):
            return uri.encode('unicode-escape')
        return uri.encode('string-escape')

    @staticmethod
    def has_schema(uri):
        parts = urlparse.urlparse(uri)
        return parts[0] != '' and parts[1] != ''

    @staticmethod
    def normalize(base_uri, uri):
        if uri.startswith('//'):
            scheme = urlparse.urlparse(base_uri)[0]
            return '{0}:{1}'.format(scheme, uri)
        if UrlUtils.is_relative(uri):
            return UrlUtils.to_absolute(base_uri, uri)
        return uri