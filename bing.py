import urllib
import urllib2
import json

from pybing import constants

class BingException(Exception): pass

class Bing(object):
    def __init__(self, app_id):
        self.app_id = app_id

    def search(self, query, source_type=None, api_version=None, **kwargs):
        kwargs.update({
            #'AppId':    self.app_id,
            #'Version':  api_version or constants.API_VERSION,
            'Query':    query,
            'Sources':  source_type or constants.DEFAULT_SOURCE_TYPE,
        })

        query_string = urllib.urlencode(kwargs)
        url = "%s?%s" % (constants.JSON_ENDPOINT, query_string)
        
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        credentials = (':%s' % self.app_id).encode('base64')[:-1]
        auth = 'Basic %s' % credentials
        request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        response = request_opener.open(request)

        data = json.load(response)
        return data

    def search_web(self, query):
        return self.search(query, source_type=constants.WEB_SOURCE_TYPE)

    def search_image(self, query):
        return self.search(query, source_type=constants.IMAGE_SOURCE_TYPE)

    def search_news(self, query):
        return self.search(query, source_type=constants.NEWS_SOURCE_TYPE)

    def search_spell(self, query):
        return self.search(query, source_type=constants.SPELL_SOURCE_TYPE)

    def search_related(self, query):
        return self.search(query, source_type=constants.RELATED_SOURCE_TYPE)

    def search_phonebook(self, query):
        return self.search(query, source_type=constants.PHONEBOOK_SOURCE_TYPE)

    def search_answers(self, query):
        return self.search(query, source_type=constants.ANSWERS_SOURCE_TYPE)
