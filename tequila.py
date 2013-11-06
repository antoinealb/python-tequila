import requests
import logging

from bs4 import BeautifulSoup

try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse

class TequilaError(RuntimeError):
    """
    Exception thrown in case of Tequila error.
    """
    pass

class TequilaConnexionWrapper(object):
    TEQUILA_LOGIN = "http://moodle.epfl.ch/login/index.php"
    TEQUILA_LOGIN_POST = "https://tequila.epfl.ch/cgi-bin/tequila/login"
    def __init__(self, username, password):
        """Explicitly login into the tequila service, this will create
        a new tequila session as self.session

        :raise TequilaError:
        """
        with requests.session() as self.session:
            resp = self.session.get(TequilaConnexionWrapper.TEQUILA_LOGIN)
            if resp.status_code != 200:
                raise TequilaError()
            parsed_url = urlparse.urlsplit(resp.url)
            dict_query = urlparse.parse_qs(parsed_url.query)
            self.sesskey = dict_query['requestkey'][0]
            payload = dict()
            payload["requestkey"] = self.sesskey
            payload["username"] = username
            payload["password"] = password

            resp = self.session.post(self.TEQUILA_LOGIN_POST,
                    verify=True, data=payload)

            soup = BeautifulSoup(resp.text)
            error = soup.find('font', color='red', size='+1')

            if error:
                logging.info("Tequila error")
                logging.debug(error.string)
                # Grab the tequila error if any
                raise TequilaError(error.string)
            if resp.status_code != 200:
                logging.info("Tequila didn't return a 200 code")
                logging.debug(resp.status_code)
                raise TequilaError()

    def get(self, *args, **kwargs):
        """
        Makes an HTTP GET request using the Tequila session.
        Same parameters as requests.get()
        """
        return self.session.get(*args, **kwargs)

    def post(self, *args, **kwargs):
        """
        Makes an HTTP POST request using the Tequila session.
        Same parameters as requests.post()
        """
        return self.session.post(*args, **kwargs)
