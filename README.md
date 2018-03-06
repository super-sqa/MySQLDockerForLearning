# MySQLDockerForLearning
## Description
Python script to run a mysql container that has sample data. 
The script will start a container with existing folders as volumes. The existing folders have the data for one database and two tables.

**Database/Schema:**

     countries

**Tables:**

    capital_city
  
    country_info
  
## Dependency
1. You must have docker installed and running on your local machine.
2. You must install Python library for the Docker Engine API
    * You can use pip to install the library.
    * You find more informtion [here](https://github.com/docker/docker-py)
    * Command to install (This is the version the script is tested with, but you can try using the latest version if a newer version is available.)
    * Both Python 2 and Python 3 are ok)
    ```
    pip install docker==3.1.0
    ```
    
## Usage
Simply run the script with python
```
$ python run_mysql_docker_container.py
```
or
```
$ python run_mysql_docker_container.py --print_docker_logs=True
```
Use command line parameter --print_docker_logs=True if you want to output of the docker commands to be displayed.
Give it time for the log to be printed. The process must finish before printing the logs.
If you do not change the settings in the script here are the parameters that will be used.
```
    CONTAINER_NAME = "ssqa_mysql"
    IMAGE = "mysql:5.6"
    ROOT_PASSWORD = "password"
```

##### Example
If the container run once before then it already exists and the script will just start it. Here is the output. Note the 'print_docker_log' is False by default.
```

$ python run_mysql_docker_container.py
Container 'ssqa_mysql' exists. Starting it.
Current status for container 'ssqa_mysql' is 'exited'. Attempting to start it.
***************************************
Started container 'ssqa_mysql'
***************************************

```

If the container does not exist but the required image exists on the local drive then here is the output.

```
Container 'ssqa_mysql' does not exist. Running new container with name 'ssqa_mysql'
Image 'mysql:5.6' exist on local drive. Starting a new container using the image.
**********************************************
Created container
Container name: 'ssqa_mysql'
Image used: 'mysql:5.6'
Root password: 'password'
Run command 'docker ps -a' to see all containers and statuses
Run command 'docker ps' to see running containers and statuses
**********************************************
```

If the image does not exist on the local machine then it will download the image. Here is example output.

```
Container 'ssqa_mysql' does not exist. Running new container with name 'ssqa_mysql'
Image 'mysql:5.6' does not exist on local drive. Downloading.... will take few minutes ......
**********************************************
Created container
Container name: 'ssqa_mysql'
Image used: 'mysql:5.6'
Root password: 'password'
Run command 'docker ps -a' to see all containers and statuses
Run command 'docker ps' to see running containers and statuses
**********************************************
```

After getting success message run a docker command on your terminal like this, to see the running container

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
659535a74243        mysql:5.6           "docker-entrypoint.s…"   12 minutes ago      Up 12 minutes       0.0.0.0:3306->3306/tcp   ssqa_mysql
```

As you can see port 3306 on the host is mapped to port 3306 in the container. Use any mysql client to connect to the database. Exmaple MySQL Workbench. If you need to use a different port, modify the script. Look for "ports" variable.


