# technical-interview-taskapp
Unfinished private coding exam



## Prerequisites:
1. Docker
2. Docker-compose
3. A web browser

## Instructions:
> This project was done on Linux, some instructions may need to change as fit depending on your OS.
1. Deploy mongo using the command
```
docker-compose up
```
2. Install the python libraries from the `requirements.txt`
> Preferrably install this in an isolated virtual enviroment.
```
pip install -r requirements.txt
```
3. Start the main application
```
python main.py
```
4. Open the interface on your web browser

Visit __localhost:7860__ for the main application interface.

And visit __localhost:8081__ to use mongo express to view the database directly.

## Whats unfinished?
1. A proper display to list collection items
2. Working update, delete and mark button
3. Full documentation

