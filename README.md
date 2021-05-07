# keygrabber

Automation for grabbing keys from a Linux host. You can use either the python2/python3 compatible script or the shell script included in this repo.

Once you gain access to a Linux host, upload this script on the host and run it and it will grab the following:

- ~/.aws/ contents
- ~/.ssh/ contents
- ~/.azure/ contents
- ~/.config/gcloud/credentials.db
- ~/.bashrc
- ~/.bash_history
- env
- gcp and aws metadata service query

## Usage
> chmod +x keygrabber.sh

OR

> chmod +x keygrabber.py

----------
> python keygrabber.py

OR

> python3 keygrabber.py

OR

> ./keygrabber.sh
