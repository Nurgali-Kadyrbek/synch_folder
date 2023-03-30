To run: 
>_python src/synchronization.py --source_path='./source_folder' --replica_path='./replica_folder' --log_path='./logs/synch1.log'  --period=10_

To stop:
>_Ctrl+C_

To test: 
>pip install pytest
>python -m pytest

**Running a Python Script in the Background**

>#!/usr/bin/env python3
>chmod +x test.py

Ignoring hangup signals.<br />
>nohup src/synchronization.py &<br />

To stop the script:<br />

>ps ax | grep synchronization.py<br />
>kill PID
