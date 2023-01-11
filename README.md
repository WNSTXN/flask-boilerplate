# flask-boilerplate

`flask-boilerplate` features improved type hints and developer ergonomics out of the box. More about Flask [here](https://flask.palletsprojects.com/).

## Requirements

- Docker

## Installation

The installation script only supports Arch or Debian-based systems. If you are on any other platform, you will have to install Docker manually [here](https://docs.docker.com/get-docker/).

```bash
sh requirements.sh
```

## Usage

```bash
sh launch.sh -n <app-name>
```

## Architecture

### Routes

Routes defined in the [routes](app/routes/) directory are automatically initialised. Each route should be defined in a separate file.

```python
# app/routes/submit_score.py

from app import App
from app.libs import SQLExtension
from app.models import User

@App.get('/submit_score')
def submit_score() -> str:
    
    username = request.form["username"]
    score = request.form["score"]
    
    player = User(username, score)
    SQLExtension.db.session.add(player)
    SQLExtension.db.session.commit()
```

### Models

All models should inherit from the [BaseModel](app/models/bases/base_model.py) dataclass. This ensures that all models are always serialisable and will never need to reimplement `id`.
