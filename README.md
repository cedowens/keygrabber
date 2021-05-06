# keygrabber

Shell script to automate grabbing keys from a Linux host. Once you gain access to a Linux host, run this script and it will grab the following:

- ~/.aws/ contents
- ~/.ssh/ contents
- ~/.azure/ contents
- ~/.config/gcloud/credentials.db
- bashrc
- .bash_history
- env
- gcp and aws metadata service query

## Usage
> chmod +x keygrabber.sh

> ./keygrabber.sh
