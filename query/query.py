
"""
This module holds the base Query class used by the various types of Bing queries.
"""

import copy
import urllib
import urllib2

import json

from pybing import constants
from pybing.query.mixin import QueryMixin

class BingQuery(QueryMixin):
    SOURCE_TYPE = None
    
    def __init__(self, app_id, query=None, version=None, *args, **kwargs):
        self.app_id = app_id
        #self.version = version or constants.API_VERSION
        self._query = "\'"+query+"\'"
        self.DEBUG = constants.DEBUG
        
        # Needed for mixin's __init__'s to be called.
        super(BingQuery, self).__init__(*args, **kwargs)
    
    def set_query(self, query):
        if not query:
            raise ValueError, 'Query cannot be empty or None'
        
        obj = self._clone()
        obj._query = query
        return obj
    
    @property
    def query(self):
        return self._query
    
    def execute(self):
        if not self.query:
            raise ValueError, 'Query cannot be empty or None'

        #elif not self.SOURCE_TYPE:
        #    raise ValueError, 'Source Type cannot be empty or None'

        from pybing.resultset import BingResultSet
        return BingResultSet(self)

    def get_request_parameters(self):
        params = super(BingQuery, self).get_request_parameters()
        params.update({
            'q':    self.query.decode('utf-8').encode('utf-8'),
            #'Sources':  source_type or constants.DEFAULT_SOURCE_TYPE,
            'mkt':  "en-us",
            'safesearch':   "Off"
        })
        return params

    def get_request_url(self):
        params = self.get_request_parameters()
        query_string = urllib.urlencode(params)
        url = constants.JSON_ENDPOINT + '?' + query_string
        return url.encode('utf-8')

    def get_search_response(self):
        data = self._get_url_contents(self.get_request_url())
        json_result = json.loads(data)
        open("test.json", 'w+').write((json.dumps(json_result, indent=4)))
        return json_result['webPages']

    def get_search_results(self):
        from pybing.result import BingResult
        response = self.get_search_response()
        return [BingResult(result) for result in response['value'] ]

    def _get_url_contents(self, url):
        user_agent = constants.USER_AGENT
        #credentials = (':%s' % self.app_id).encode('base64')[:-1]
        #auth = 'Basic %s' % credentials
        
        request = urllib2.Request(url)
        #print(url)
        request.add_header('Ocp-Apim-Subscription-Key', self.app_id)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        if self.DEBUG:
            print "API endpoint url: %s" % url
        response = request_opener.open(request)
        return response.read()

    def _clone(self):
        """
        Do a deep copy of this object returning a clone that can be
        modified without affecting the old copy.
        """
        return copy.deepcopy(self)

    def __unicode__(self):
        return u'BingQuery: %s' % self.get_request_url()

    __str__ = __unicode__

    def __repr__(self):
        return u'<%s>' % unicode(self)
