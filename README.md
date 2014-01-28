# python-tequila
A python wrapper for the Tequila Login Manager at EPFL. Based on original work by
@gcmalloc.

## Usage

To get a connexion :

    conn = TequilaConnexionWrapper("gaspar" ,"secret")

To fetch a page content :

    response = conn.get("http://moodle.epfl.ch")

The response is a python requests reponse object, so check its documentation to
know how to use it.

## Requirements
* `BeautifulSoup`
* `requests`




