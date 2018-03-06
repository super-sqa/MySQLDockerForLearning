# MySQLDockerForLearning
### Description
Python script to run a mysql container that as some sample data. 
The script will start a container with existing folders as volumes. The existing folders have information for one database and two tables.
**Database/Schema: countries**
**Tables:**
  capital_city
  country_info
  
### Dependency
1. You must have docker installed and running on your local machine.
2. You must install Python library for the Docker Engine API
    * You can use pip to install the library.
    * You find more informtion [here](https://github.com/docker/docker-py)
    * Command to install (This is the version the script is tested with. Both Python 2 and Python 3 are ok)
    ```
    pip install docker==3.1.0
    ```
    
### Usage
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
If the container run once before then there is the output. Note the 'print_docker_log' is False by default.
```
$ python run_mysql_docker_container.py

```
After the script complete you should get a success message or failure message.

After getting success message run a docker command on your terminal like this, to see the running container
```
Container 'ssqa_mysql' exists. Starting it.
Current status for container 'ssqa_mysql' is 'exited'. Attempting to start it.
***************************************
Started container 'ssqa_mysql'
***************************************
```

