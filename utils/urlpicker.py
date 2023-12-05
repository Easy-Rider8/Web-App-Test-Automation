from config.settings import Configuration


def select_url():

    match Configuration.BASE_URL:
        case 'prod':
            url = Configuration.PROD_URL
        case 'test':
            url = Configuration.TEST_URL
        case 'local':
            url = Configuration.LOCAL_URL
        case _:
            raise ValueError("URL you entered '" + Configuration.BASE_URL + "' is invalid option")
    return url