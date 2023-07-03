# 'Suggested Links' Figma Plugin Backend

This repository contains code for a Python server that functions as backend for the 'Suggested Links' Figma plugin.
It receives a list of hierarchical screen data from the plugin's frontend and returns a list of suggested links based on the used link prediction model.

This application is part of a publication titled "Interactive Link Prediction as a Downstream Task for Foundational GUI Understanding Models" by [Christoph A. Johns](mailto:christophjohns@aalto.fi?subject=[GitHub]%20Suggested%20Links%Figma%Plugin) at Aarhus University.
The project was supervised by Michael Barz at German Research Center for Artificial Intelligence (DFKI).

## Development

To start the server, run:

```zsh
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run
```

To expose the local port for remote use, run:

```zsh
$ lt --port 3000
```
