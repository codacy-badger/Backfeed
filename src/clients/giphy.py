
import giphy_client as giphy

__all__ = ['search']


def search(term: str = '', key: str = '', limit: int = 1, rating: str = 'g', lang: str = 'en') -> dict:
    '''
        Search for gifs on Giphy

        Parameters
        ----------

        key:
            Client private key

        term:
            Search term

        limit:
            Limit of resources

        rating:
            Results by specified rating

        lang:
            Language for regional content

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

    response = giphy.DefaultApi().gifs_search_get(
        key, term, limit=limit, rating=rating, lang=lang)

    try:
        if response.meta.status == 200:
            return response.to_dict()

        return {}
    except Exception as e:
        raise Exception(str(e))
