
from json import dumps

__all__ = ['pretty']


def pretty(dictionary: dict, indent: int = 2, sort_keys: bool = True) -> dict:
    '''
        Format a dict

        Parameters
        ----------

        dictionary:
            Arbitrary dict

        indent:
            Tabulation level

        sort_key:
            Sort dict keys

        Usage
        -----

        >>> pretty({'key': 'value'}, 4, False)
    '''

    try:
        return dumps(dictionary, indent=indent, sort_keys=sort_keys)
    except Exception as e:
        raise Exception(str(e))
