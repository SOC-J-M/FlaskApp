import requests

api_url = "http://127.0.0.1:5000/data" 
record = {"key": 5000, # int AI PK
		"time_stamp": "2025-01-01 00:00:00", # datetime
		"reporting_node": "foo", # varchar(45)
		"department": "foo", # varchar(45)
		"work_center": "foo", # varchar(45)
		"employee_id": "foo", # varchar(45)
		"part_number": "foo", # varchar(45)
		"quantity": 1, # int
		"work_order": "foo", # varchar(45)
		"start_time": "1000-01-01 00:00:00", # time
		"end_time": "1000-01-01 00:00:00", # time
		"sequence_num": "foo", # varchar(45)
		"progress": "foo", # varchar(45)
		"setup_time": "foo", # varchar(45)
		"die_set": "foo", # varchar(45)
		"material_lot": "foo", # varchar(45)
		"status_code": "foo", # varchar(45)
		"comments": "request 1", # varchar(500)
		}

response = requests.post(api_url, json=record)
response.json()