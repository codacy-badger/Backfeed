#### Backfeed

---

> General content platform :flower_playing_cards:

Connection between multiple APIs and ML applicated

#### To Do

- [ ] Add clients

  - Spotiy, Sound Cloud, Musix Match and Genius

  - Fanart Tv, Tv Show Time, Imdb and Youtube

- [ ] Deep Learning model

- [ ] Authentication and authorization (OAuth)

- [ ] Front-end views (Jinja, React or Vue)

- [ ] NoSQL database (Elasticsearch or Mongo)

- [ ] Scraper to populate the database

- [x] User persona

**Obs**: [APIs](https://www.programmableweb.com/apis/directory)

#### Setup

The project was built on Linux platform using virtual environments.

##### Requirements

- Requests

- Giphy Client

##### Instructions

1. Create the virtual environment

```sh
virtualenv python3.7 venv
```

2. Install the dependencies on virtual environment

```sh
pip install -r requirements.txt
```

3. Start the server

```sh
python wsgi.dev.py # wsgi.dev
```

**Obs**: To activate and deactivate the virtual environment use `source venv/bin/activate` and `deactivate`.

#### Tree

- _settings_ -> configurations

- _requirements_ -> dependencies

- _src_ -> code implementation

  - _utils_ -> useful scripts

  - _clients_ -> content

  - _api_ -> authorization, authentication and back-end interface

#### Notes

This is a side project, every pull request is well accepted.
