# [Slack]

This is a Slack application for managing users and channels in Slack workspace.\
The code written in python.🐉\
Run on docker.🐋

## Installation ⬇️

✔️ Clone to code.

✔️ Navigate into project directory.

✔️ Run the service by running :

Build  image

```bash
docker build . -t < image_name > 
```

Run docker container  

```bash
docker run -it --entrypoint bash -v ${pwd}:/app < image_name >
```

✔️ Change *const* variables and *.env* file.

## Usage ✍

Run `python slack_client.py`

[Slack]:https://api.slack.com/automation/quickstart
