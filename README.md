# python-tequila
A python wrapper for the Tequila Login Manager at EPFL. Based on original work by
@gcmalloc.

## Usage

To get a requests session which is authenticated against Tequila.

    conn = create_tequila_session("gaspar", "secret")

`conn` is a [session](http://docs.python-requests.org/en/latest/user/advanced/#session-objects) 
object. For example, to fetch a page content :

    response = conn.get("http://moodle.epfl.ch")

The response is a python requests reponse object, so check its documentation to
know how to use it.

## Requirements
* `BeautifulSoup`
* `requests`




