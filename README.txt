Create AWS account 
Create IAM > create topic.

Subscribe to to topic to get email notifications
-Go to your email, open AWS subscription confirmation and click subscribe to topic.

Install Python 
-Go to https://www.python.org/downloads/.
-Download and install Python.

Install Windows terminal
-Go to https://docs.microsoft.com/en-us/windows/terminal/install.
-Install Windows terminal.

Create S3 bucket
-Type windows terminal on windows search bar and click on windows terminal to open.
-On terminal, type: pip install boto3 and press enter.
-On terminal, type: cd Desktop and press enter > cd sn_systems and press enter > 
python s3_uploader.py and press enter.

Create event notifications 
-Go to https://aws.amazon.com/console/

-Enter the following credentials to log in:
Account ID (12 digits) or account alias:  ie. 94069xxxxxx
IAM user name:  USERNAME.
password aim user: enter your password.

-Find S3 > your bucket >properties > events notifications > create notifications > name your event > check 'put' checkbox > destination > choose SNS > from drop down menu choose 'Uploader > save changes.

Download and install S3 browser
-Go to https://s3browser.com/ , download and install the software.

-Enter the following credentials to log in:
access key =          your access key.
secret access key =   your secret access key.

-Click on your bucket > click buckets tab > click lifecycle configuration from drop down menu > click add > actions current version tab > permanently delete files > choose how many days you like to keep your files > check enable checkbox > click add new rule.

How to upload files 
-Click S3 browser Desktop icon to run sofware.
-Click upload > upload file > choose file >click open.