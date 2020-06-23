# School administration teacher directory

Welcome !  
With this tool you can :  
- Add study field  
- Add teacher individually
- Add teachers ***in bulk*** using CSV files  
- Sort teachers by subjects they teach, or/and by name

### Requirements
- Python > 3.7  

### Quickstart
- `pip install -r requirements.txt`  
- `python manage.py runserver`
- Hit ***http://127.0.0.1:8000/directory***

### CSV file structure
![CSV file for bulk insert structure](/directory/static/csv-structure.png "CSV file for bulk insert structure")

##### Developer's corner
Wanna make sure everything is alright ?  
Run `python manage.py test`