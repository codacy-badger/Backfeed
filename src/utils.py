
from flask import jsonify

from json import dumps

__all__ = ['pretty', 'catch_404', 'catch_500']


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

        Return
        ------

        Formated dict
    '''

    try:
        return dumps(dictionary, indent=indent, sort_keys=sort_keys)
    except Exception as e:
        raise Exception(str(e))


def catch_404(error):
    '''
        Catch not found pages

        Parameters
        ----------

        error:
            The error caught up by Flask (http status code)

        Usage
        -----

        None

        Return
        ------

        Key value object contaning a error massage
    '''

    return jsonify(catch='page not found')

def catch_500(error):
    '''
        Catch server internal errors

        Parameters
        ----------

        error:
            The error caught up by Flask (http status code)

        Usage
        -----

        None

        Return
        ------

        Key value object contaning a error massage
    '''

    return jsonify(catch='internal error')