#!/usr/bin/env python3

import requests
import subprocess

def jfrogUpload():
    # Define the URL, file path, and authentication credentials
    url = 'http://35.173.125.244/:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/Jenkinns_pipeline/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Ul123456'  # Replace 'your_password' with the actual password

    # Send the PUT request with authentication and file upload
    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)

    # Check the response status code
    if response.status_code == 201:
        print("\nPUT request was successful!")
    else:
        print(f"PUT request failed with status code {response.status_code}")
        print("Response content:")
        print(response.text)

def mvnBuild():
    # Define the Maven command
    maven_command = "mvn clean install -DskipTests"

    # Run the Maven command as a subprocess
    try:
        subprocess.run(maven_command, check=True, text=True, shell=True)
        print("\nMaven build completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Maven build failed with exit code {e.returncode}")


def main():
#    mvnBuild()
    jfrogUpload()

##############################################################################################################
if __name__ == "__main__":
    main()
