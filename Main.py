from application.salary import calculate_salary 
from application.db.people import get_employees  
import datetime
import requests


if __name__ == '__main__':
  calculate_salary()
  get_employees()
  print(datetime.date.today())
  r = requests.get('https://google.com')
  print(r.status_code)
  
