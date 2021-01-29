This AWS lambda function makes a database query from an existing RDS MYSQL database and prints the query to the cloudwatch logs.

PyMySQL was used for this code so I've included the packages in this repo for it >> you have to zip these files and upload them into lambda for it to work

Used a secrets file for passing in sensitive values such as db credentials and db queries