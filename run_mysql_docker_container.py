"""
Script to run a mysql docker container.
- It will mount volumes relative to this script for mysql config and for mysql data.
- Will download mysql image and run it with given name
- If the image already exists used the existing image
- If container with the given name exists it starts the container
"""

import docker
import time
import argparse
import os


class DockerRunner(object):

    def __init__(self, docker_logs):
        self.client = docker.from_env()
        self.docker_logs = docker_logs

        # check if docker is running
        try:
            self.client.ping()
        except Exception as e:
            raise Exception("Got an Exception. Is docker running. Error message: {}".format(str(e)))


    def does_container_exist_by_name(self, name):
        """
        Method to check a container with the given name exists.
        Will return True or False if container exists or not respectively.
        :param name: name of container
        :return: bool
        """

        all_containers = self.client.containers.list(all=True)

        all_container_names = [container.name for container in all_containers]

        if name in all_container_names:
            return True
        else:
            return False

    def does_local_image_exist(self, image):
        """
        Method to check if the given image exists on local driver.
        The image name should contain the tag.
        :param image: image name with tag. Example 'mysql:5.6' or 'mysql:latest'
        :return: bool
        """

        images_list = self.client.images.list()
        image_tags = [i.tags for i in images_list]
        for tags in image_tags:
            if image in tags:
                break
        else:
            return False

        return True

    def start_my_container(self, container_name):
        """
        Starts container that has the given name.
        If it fails to start the container it will raise an exception.
        :param container_name: name of container to start
        :return: None
        """
        my_container = self.client.containers.get(container_name)
        status = my_container.status
        if status == 'running':
            print("Container '{}' is already running. Run command 'docker ps' to see details.".format(container_name))
        else:
            print("Current status for container '{}' is '{}'. Attempting to start it.".format(container_name, status))
            my_container.start()
            time.sleep(4)
            # after starting check the status of the container again
            my_container = self.client.containers.get(container_name)
            status = my_container.status
            if status != 'running':
                raise Exception("Failed to start container '{}'. Current status '{}'".format(container_name, status))

    def main(self, expected_container_name, image, root_password):
        """
        Main method. It will start or create a container with the given name based on the given image.
        :param expected_container_name: name of container expected to exist or to create
        :param image: image to use for the container. Example "mysql:5.7"
        :param root_password: mysql password for the 'root' user
        :return: None
        """
        does_container_exist = self.does_container_exist_by_name(expected_container_name)
        if does_container_exist:
            print("Container '{c_name}' exists. Starting it.".format(c_name=expected_container_name))
            self.start_my_container(expected_container_name)
            print("***************************************")
            print("Started container '{}'".format(expected_container_name))
            print("***************************************")
        else:
            print("Container '{c_name}' does not exist. Running new container with name '{c_name}'".format(c_name=expected_container_name))

            # check if the images is available on local drive. If not new image will be downloaded (takes time)
            exists = self.does_local_image_exist(image)
            if exists:
                print("Image '{}' exist on local drive. Starting a new container using the image.".format(image))
            else:
                print("Image '{}' does not exist on local drive. Downloading.... will take few minutes ......".format(image))

            # Specify volume mapping. Volumes are we keep persistent data and custom configs
            volumes = {os.path.join(os.getcwd(), "mysql_volumes", "configurations"): {'bind': '/etc/mysql/conf.d', 'mode': 'rw'},
                       os.path.join(os.getcwd(), "mysql_volumes", "data"): {'bind': '/var/lib/mysql', 'mode': 'rw'}}
            environment = {"MYSQL_ROOT_PASSWORD": root_password}
            ports = {"3306/tcp": "3308"}

            # run the container
            container = self.client.containers.run(image,
                                                   name=expected_container_name,
                                                   environment=environment,
                                                   ports=ports,
                                                   volumes=volumes,
                                                   detach=True,
                                                   stdout=True)
            if self.docker_logs:
                time.sleep(4)
                logs = container.logs()
                logs_split = logs.split('\n')
                for line in logs_split:
                    print(line)

            # print useful message to the user
            print("**********************************************")
            print("Created container")
            print("Container name: '{}'".format(container.name))
            print("Image used: '{}'".format(image))
            print("Root password: '{}'".format(root_password))
            print("Run command 'docker ps -a' to see all containers and statuses")
            print("Run command 'docker ps' to see running containers and statuses")
            print("**********************************************")


if __name__ == '__main__':
    # entry point to the script

    # set user variables
    CONTAINER_NAME = "ssqa_mysql"
    IMAGE = "mysql:5.6"
    ROOT_PASSWORD = "password"

    # get command line argument (Optional)
    parser = argparse.ArgumentParser()
    parser.add_argument('--print_docker_logs',
                        default='False',
                        choices=['FALSE', 'TRUE'],
                        type=str.upper,
                        required=False,
                        help="Option to print the output of docker commands to console.")

    args = parser.parse_args()
    print_docker_logs = True if args.print_docker_logs == 'True' else False


    # Create object and run main
    my_obj = DockerRunner(print_docker_logs)
    my_obj.main(CONTAINER_NAME, IMAGE, ROOT_PASSWORD)