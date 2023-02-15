# Flask with Mysql in Beanstalk

To deploy a Python Flask application with MariaDB on Elastic Beanstalk, you can create an Elastic Beanstalk configuration file with the necessary settings. 

# Configs
Root/.ebextensions/
- 01_packages.config - This will install the necessary packages for building the mysqlclient Python package, which is required to connect to MariaDB.
 - 02_environment.config - This will set the environment variables FLASK_APP and FLASK_ENV for your Flask application, as well as the DATABASE_URL variable for connecting to MariaDB. Replace <username>, <password>, <hostname>, <port>, and <database_name> with your actual MariaDB credentials.

Root/
 - .ebignore - files/folders to not package to AWS

With these configuration files in place, you can deploy your Flask application to Elastic Beanstalk and it should automatically connect to MariaDB using the DATABASE_URL environment variable.

# Deploy
At this point we can follow https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html to deploy using the cli