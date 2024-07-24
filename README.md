# KONG Checker Path

The tool to get all paths that configured in KONGs.

![](templates/1.jpg "")

## Create a virtual environment 
```
python -m venv env
```

## Activate the virtual environment

### Windows
```
env\Scripts\activate
```

### macOS and Linux
```
source env/bin/activate
```

## Development

```
pip install -r requirements.txt
python app.py
```

`.env`

List of KONG routes
```
API_URLS=http://192.168.0.253:8080/kong/1.json,http://192.168.0.253:8080/kong/2.json
```

## Deployment

### Docker

The pre-built image is: https://hub.docker.com/r/leqnam/kong-paths-fillter/tags

Run in Docker:
```
docker pull leqnam/kong-paths-fillter:0.0.2-alpha
docker run -p 5000:5000 --env-file "C:\.env" leqnam/kong-paths-fillter:0.0.2-alpha
```

### K8s