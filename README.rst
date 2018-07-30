================
Weather App v1.0
================

Description:
============



**Run application from Docker image:**

To run app as docker container (Docker have to be installed on the local machine):
::
 - Pull docker image from https://hub.docker.com/r/dockermariusz/kata-project-new/
 - $ docker run -e GOOGLE_API_KEY=your_google_api_key -e OWM_API_KEY=your_owm_api_key --name 
     weather-app -p 8000:8080 dockermariusz/kata-project-new:latest
 - open http://localhost:8000





