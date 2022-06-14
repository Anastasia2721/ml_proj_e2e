# Final Project: End-to-End Sample ML Project 
## Contents:
1. Source data information
2. The model
3. VM without using Docker
4. Info about Dockefile
5. How to build a Docker container

## 1.Source Data Information
We used data from [Yandex.Realty](https://realty.yandex.ru) about real estate prices in St. Petersburg for the period of Jan 2017 to Aug 2018.
We have treated data for outliers in the original dataset. The cleaned dataset is contained in the file **E2E cleaned_dataset.csv**. The code used is stored under **E2E final model.ipynb**. 
![image1.png](materials/image1.png)
![image2.png](materials/image2.png)

## 2.The model
We were required to have two models in this exercise, so we have used two models RandomForestRegressor and CatBoostRegressor to build two different models with the same variables. 
RandomForest used parameters such as:

- Room count – int
- Area – float
- Kitchen area – float
- Renovation – bool

CatBoost used:
- Room Count
- Area
- Ratio

The model used was RandomForestRegressor, because it showed less overfitting   

## 3. How to install instructions and run an app with virtual environment (without a docker)

Once you have created and connected to your VM, you can create you virtual environment **(without a docker)**:
1. `sudo apt install python3.8-venv`
2. `python3 -m venv env`
3. `source env/bin/activate`

You will also need to initialize a git repository in your virtual environment. To do this, you need to run:
1. `sudo apt install git` 
2. `git clone https://github.com/Anastasia2721/ml_proj_e2e.git`
3. `cd ml_proj_e2e`

Now you can pull the files from this repository. Afterwards you will need to install requirements from requirements.txt file by executing: `pip install -r requirements.txt`.

Examples of REST API call you can find in the `rest-api.http`.

## 4. Information about Dockerfile

You may want to have a look at **Dockerfile** in the repository. 
```linux
FROM python:3.8-slim-buster
WORKDIR /python-docker
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
```
We used `python` image to create our docker containers. Code copies all the content, installs all the required libraries stored in `requirements.txt`, and runs an application `app.py`.

## How to build container using docker
Use the set of the following commands to make and launch the containers:
Build the container:

    docker build --tag st095434/ml_proj_e2e:v1.0 .
    
Launch the container:

    docker run --network host -d st095434/ml_proj_e2e:v1.0
Now the container is running!
You can use the same search query as before.

To exit the container you need to use *exit* command while inside of the container

To see the active containers use

    docker ps
To stop the container you need to use the callsign of this container and write in code:

    docker stop <container name>
 You can also push it to your container using the docker push command:
 

    docker push st095434/ml_proj_e2e:v1.0
