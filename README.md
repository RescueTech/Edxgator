# edxgator

Edx course aggregator - Advanced edx filtration system. Check out the project's [documentation](http://zee93.github.io/edxgator/).

This project is built using the following tech:

- MongoDB
- starlette
- uvicorn


This architecture of the project:

we have two main modules, the API, and the gateway. The API si the interface to the frontend and is responsible for the 
interactions with it. It's also responsible for interacting with the gateway which takes the raw data from the API,
and processes it before sending it to the mongo database.

There's currently, the third submodule called `ui`, but it's to be removed soon.

---
Important commands:

- server: `python -m api runserver`
- sync edx: `python -m sync_edx`