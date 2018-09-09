
from flask import Flask

from .utils import catch_404, catch_500


def create_app() -> None:
    '''
        Create, configure and return a Flas app

        Parameters
        ----------

        None

        Usage
        -----

        >>> create_app()

        Return
        ------

        None
    '''

    # Instantiate a new application

    app = Flask('Backfeed')

    # Register errors handler

    app.register_error_handler(404, catch_404)

    app.register_error_handler(500, catch_500)

    return app
