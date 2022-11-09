# simplify-scraper

looking for jobs right now. I use the simplify chrome extension to fill in and help keep track of applications. It stores the data fine, but I want to analyze my applications. It isn't possible to download data from the app's webpage. this app will be able to parse each posting and then load it into a csv.

# instructions
developed on Python 3.9.12
1. `pip install requirements.txt`
1. download rendered html from Simplify using the inspect tool.
2. put all those htmls in the tasks directory
3. run `python app.py` and it will output those applications to the output.csv

### if docker installed

1. docker pull python 3.9.12
2. docker run -d -t --name simplify-scraper --mount type=bind,source="$(pwd)"/target,target=/app python:3.9.12
3. docker exec -it simplify-scraper bash
    in bash:
    1. cd app
    2. pip install -r requirements.txt
    3. python app.py
    4. exit # to exit docker conta
4. docker stop simplify-scraper

# future changes
adding each app card to the csv as they are read in. this will improve memory. it isn't a big concern because I don't expect 1000s of applications. adding these cards to a database will be good too as they are added


*Connor Lydon*