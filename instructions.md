Here are the instructions you need to follow
to run the Framework for executing the provided 
E2E tests, developed using Python & Selenium

# System
Ubuntu > 16.04

# Preconditions
```
sudo apt-get install git
sudo apt-get install openjdk-6-jdk
sudo apt-get install python-pip python-dev build-essential
```

# Installing virtual env
```
sudo pip install virtualenv 
sudo pip install virtualenvwrapper
```

# Installing e2e framework dependencies
```
sudo apt-get install xserver-xephyr
sudo apt-get install xvfb
sudo apt-get install chromium-chromedriver
```

##### Downloading the project
Into your local machine, if it doesn't exist, 
create a common code folder. 
For example "/home/youruser/apps/"

```
cd /home/youruser/
mdkir apps
```
Access to this folder. Example "cd /home/youruser/apps/"
Then download the repository using GIT
```
git clone https://github.com/packlink-dev/qa_code_challenge_juanmaperez85.git
```

Check that a new folder has been created
Example: /home/youruser/apps/qa_code_challenge_juanmaperez85/

# Creating the virtual environment
Using "workon" or "virtualenv", create the virtual environment

It should be created out of the project folder.

Example where it should be created "/home/youruser/apps/"

```
virtualenv _env_e2e

```

Normally, the virtual environment is activated by default.
In your console you should see something similar to:
"(_env_e2e) youruser@XXX:~/apps/qa_code_challenge_juanmaperez85"

BTW, you could activate it manually accessing to your code folder. 
Example: "cd /home/youruser/apps/qa_code_challenge_juanmaperez85" 

And THEN activating it. 
Example: ". ../_env_e2e/bin/activate"


# Add the ChromeDriver path into your local environment
Open your activate file in an editor

```
# Example using nano editor
nano /home/your_user/code/e2e/_env_e2e/bin/activate
```
Then add the information below at the end of the activate file:

```
#Path to chromedriver
export CHROMEDRIVER_PATH="/usr/lib/chromium-browser/chromedriver"
```
It is recommended to restart the virtual environment, so, 
deactivate your virtual environment and activate it again 
(Example: ". ../_env_e2e/bin/activate")

##### Install pip dependencies
Into the "apps/qa_code_challenge_juanmaperez85" folder execute:
```
pip install -r requirements.txt
```

# Example for executing all features from the project folder
Into the project folder, with the virtual env activated:
```
python manage.py test qa_code_challenge_juanmaperez85 --settings=integration_tests.settings.e2e
```

