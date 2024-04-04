import serial
from datetime import datetime, timedelta
import requests

def isValidOrder(num):
    return num > 0

def push_data(input, dept, work_c, work_o, part):
    count = int(input[0])
    elapsed_time = int(input[1])
    status_code = input[2]

    end_time = datetime.now()
    start_time = end_time - timedelta(milliseconds=elapsed_time)

    end_time = end_time.strftime("%H:%M:%S")
    start_time = start_time.strftime("%H:%M:%S")

    curr_time = datetime.now().isoformat()
    api_url = "https://pq8gj1sm4k.execute-api.us-west-1.amazonaws.com/api/data" 
    record = {
		"time_stamp": curr_time, # datetime
		"reporting_node": "foo", # varchar(45)
		"department": dept, # varchar(45)
		"work_center": work_c, # varchar(45)
		"employee_id": "foo", # varchar(45)
		"part_number": str(part), # varchar(45)
		"quantity": count, # int
		"work_order": work_o, # varchar(45)
		"start_time": start_time, # time
		"end_time": end_time, # time
		"sequence_num": "foo", # varchar(45)
		"progress": "foo", # varchar(45)
		"setup_time": "foo", # varchar(45)
		"die_set": "foo", # varchar(45)
		"material_lot": "foo", # varchar(45)
		"status_code": status_code, # varchar(45)
		"comments": "request 1", # varchar(500)
		}
    response = requests.post(api_url, json=record)
    response.json()

#modify this to read from the serial monitor
    
if __name__ == "__main__":
    department = ""
    work_center = ""
    work_order = -1
    part_number = ""

    while len(department) < 2:
        department = input('Department: ')
    while len(work_center) < 2:
        work_center = input('Work center: ')
    while not isValidOrder(work_order):
        try: 
            work_order = int(input('Work order: '))
        except:
            work_order = -1
    while len(part_number) < 2:
        part_number = input('Part number: ')


    # arduino1_port = "/dev/cu.usbmodemF412FA636CFC2"
    # arduino1_baudrate = 9600
    # arduino = serial.Serial(arduino1_port, arduino1_baudrate)

    # while True:
    #     text = arduino.readline().decode('utf-8').strip()
    #     text_read = text.split(",")

    #     push_data(text_read, department, work_center, work_order, part_number)
    
    data = [23, 1250, "Active"]
    push_data(data, department, work_center, work_order, part_number)