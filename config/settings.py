class Configuration(object):
    BROWSER = 'chrome' # or "firefox", "safari", "ie", "edge" etc.
    BASE_URL = 'test' # or "prod", "local"

    PROD_URL = "https://*prod_url*"
    TEST_URL = "https://*test_url"
    LOCAL_URL = "https://*local_url*"

    IMPLICIT_WAIT = 10