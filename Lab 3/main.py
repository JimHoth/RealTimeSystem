print("Hello LAB3")

import time
from task1 import *
from scheduler import *

scheduler = Scheduler()
scheduler.SCH_Init()

task1 = Task1(0)
task2 = Task1(1) 

scheduler.SCH_Add_Task(task1.Task1_Run, 0, 3000)
scheduler.SCH_Add_Task(task2.Task1_Run, 2000, 3000)



while True:
    scheduler.SCH_Update()
    scheduler.SCH_Dispatch_Tasks()
    time.sleep(0.1)

