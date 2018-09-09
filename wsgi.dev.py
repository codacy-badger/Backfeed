
from src import create_app

if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=5000, debug=True,
                     use_reloader=True, ssl_context='adhoc', threaded=True)  # processes
