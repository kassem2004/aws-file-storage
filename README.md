# aws-file-storage

The goal for this project is to create a secure file storage and access management system using AWS, Python and SQL.

I will be using AWS S3 for storing the actual files, Python to write the scripts for the interactions with AWS and the SQL database, and a PostgreSQL database to store the metadata like access logs, fileID and associated userID, etc.

I will also be documenting the journey here, first step has been to just create a local PostgreSQL database, and have a python script that can interact with it, which is now complete in the db_connection.py file. I used enviroment variables to hide sensitive information.

Next step will be to add AWS S3.

Successfully Integrated AWS S3 services, I can now create a bucket and add objects via my python scripts. The set up of the system is now complete, I am able to interact with both S3 and SQL Database via Python scripts.

Next steps will be to start cleaning up the code, and adding security via other AWS Services, and other security methods like automated audits etc.
