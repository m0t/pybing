#API_VERSION = '2.0'
JSON_ENDPOINT = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
MAX_PAGE_SIZE = 50
MAX_RESULTS = 1000
USER_AGENT= 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)' #hihi
DEBUG = False

WEB_SOURCE_TYPE = 'Web'
IMAGE_SOURCE_TYPE = 'Image'
NEWS_SOURCE_TYPE = 'News'
SPELL_SOURCE_TYPE = 'Spell'
RELATED_SOURCE_TYPE = 'RelatedSearch'
PHONEBOOK_SOURCE_TYPE = 'Phonebook'
ANSWERS_SOURCE_TYPE = 'InstanceAnswer'

SOURCE_TYPES = (
    WEB_SOURCE_TYPE,
    IMAGE_SOURCE_TYPE,
    NEWS_SOURCE_TYPE,
    SPELL_SOURCE_TYPE,
    RELATED_SOURCE_TYPE,
    PHONEBOOK_SOURCE_TYPE,
    ANSWERS_SOURCE_TYPE,
)

DEFAULT_SOURCE_TYPE = WEB_SOURCE_TYPE