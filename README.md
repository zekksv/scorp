### Get Started

- Flask application is coded to accomplish tasks provided by Scorp.
- If venv which is inside the project is activated there is no need to install any dependencies otherwise following dependencies must be installed

    `pip install mysql-connector-python`
  
- There is a file called constants.py under the helpers directory which holds constants for configurations. Following lines must be edited based on your configuration.
    ```
    MYSQL_USER = "root"
    MYSQL_PASS = ""
    MYSQL_DB = "scorp_case_study"
    MYSQL_HOST = "127.0.0.1"
	```
- To run the project following command should be used inside the project folder.
  
	`python app.py`
	
- After running the project, server will start to listen for request at "http://127.0.0.1:5000/"
	
- Example requests can be shown in .pngs provided.

- Note: Sql file is also provided and must be imported to sql server that you are using for project to run properly.
