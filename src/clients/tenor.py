
from requests import get

__all__ = ['search']


def search(term: str = '', key: str = '', limit: int = 1) -> dict:
    '''
        Search for gifs on Tenor

        Parameters
        ----------

        key:
            Client private key

        term:
            Search term

        limit:
            Limit of resources

        Usage
        -----

        >>> search(key='', term='')

        Return
        ------

        Dict containing gif data
    '''

    if term == '' or key == '':
        raise Exception('Couldn\'t find the {0}key{1} or the {0}term{1}'.format(
            '\033[31m', '\033[37m'))

    with get(f'https://api.tenor.com/v1/anonid?key={key}') as anonymous_id:
        if anonymous_id.status_code == 200:
            anon_id = anonymous_id.json()['anon_id']
        else:
            anon_id = ''

    with get(f'https://api.tenor.com/v1/search?q={term}&key={key}&limit={limit}&anon_id={anon_id}') as response:
        if response.status_code == 200:
            return response.json()

        return {}
