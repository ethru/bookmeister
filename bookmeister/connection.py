"""#### Connection

Module with `Database` class which gathers methods necessary to communicate
with database REST API. It allows to add, search, update or delete records. To
perform those operations `requests` module is used. Every method confirms its
result by returning True or expected data. In case of error False or None is
returned. Values received or sent to database are converted with `json` module.


#### License
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from json import dumps, loads

import requests


class Database:
    """
    A class containing methods needed for communication with database.

    ...

    Attributes
    ----------
    url : str
        database address
    collection : str
        name of collection in database
    headers : dict
        dictionary containing information send with request to database
    """

    def __init__(self):
        """Initialize basic settings needed for communication with database."""
        self.url = 'https://bookstore-5217.restdb.io'
        self.collection = '/rest/books'
        self.headers = {
            'content-type': 'application/json',
            'x-apikey': '5e5f9cf028222370f14d4ece',
            'cache-control': 'no-cache',
        }

    def add(self, values):
        """Send values to database.

        Parameters
        ----------
        values : dict
            dictionary with names of fields and their values to store

        Returns
        -------
        bool
            True when record added to database else False
        """
        try:
            response = requests.request(
                'POST',
                self.url + self.collection,
                data=dumps(values),
                headers=self.headers
            )
            return '_id' in response.text
        except requests.exceptions.ConnectionError:
            return False

    def search(self, parameters):
        """Search for records matching `parameters` in database.

        Parameters
        ----------
        parameters : dict
            dictionary with names of fields and values which will be searched
            in database

        Returns
        -------
        List
            list with records matching criteria
        None
            when connection error occurs
        """
        query = f'?q={dumps(parameters)}'
        try:
            response = requests.request(
                'GET',
                self.url + self.collection + query,
                headers=self.headers
            )
            return loads(response.text)
        except requests.exceptions.ConnectionError:
            return None

    def delete(self, record_id):
        """Remove record from database.

        Parameters
        ----------
        record_id : str
            key of record to remove

        Returns
        -------
        bool
            True when record removed from database else False
        """
        try:
            response = requests.request(
                'DELETE',
                self.url + self.collection + '/' + record_id,
                headers=self.headers
            )
            return record_id in response.text
        except requests.exceptions.ConnectionError:
            return False

    def update(self, record_id, values):
        """Update record in database.

        Parameters
        ----------
        record_id : str
            key of record to update
        values : dict
            dictionary with names of fields and values to change in database

        Returns
        -------
        bool
            True when record modified in database else False
        """
        try:
            response = requests.request(
                'PATCH',
                self.url + self.collection + '/' + record_id,
                data=dumps(values),
                headers=self.headers
            )
            return record_id in response.text
        except requests.exceptions.ConnectionError:
            return False

    def upload_image(self, path):
        """Upload image to database media archive.

        Parameters
        ----------
        path : str
            image path

        Returns
        -------
        str
            id of uploaded image
        None
            when connection error occurs or no id in response
        """
        headers = self.headers.copy()
        headers.pop('content-type', None)
        try:
            response = requests.request(
                'POST',
                self.url + '/media',
                files={'image': open(path, 'rb')},
                headers=headers
            )
            return loads(response.text)["ids"][0]
        except (TypeError, KeyError, requests.exceptions.ConnectionError):
            return None
