
"""
This module holds the Bing WebQuery class used to do web searches against Bing.

I dont think any of this is supported anymore in the new cognitive services
"""

from pybing import constants
from pybing.query import BingQuery, Pagable


class WebQuery(BingQuery, Pagable):
    #SOURCE_TYPE = constants.WEB_SOURCE_TYPE
    pass

class FileTypeQuery(WebQuery):
    def __init__(self, app_id, query=None, filetype=None, version=None, *args, **kwargs):
        self.filetype = filetype
        super(FileTypeQuery, self).__init__(app_id, query, version, *args, **kwargs)


    def get_request_parameters(self):
        params = super(FileTypeQuery, self).get_request_parameters()
        '''
        XXX can be fixed by introducing a filetype: operator in the query
        params.update({
            'WebFileType': "\'"+ self.filetype.upper() + "\'",
            'WebSearchOptions' : "'DisableHostCollapsing'" 
        })'''
        return params

