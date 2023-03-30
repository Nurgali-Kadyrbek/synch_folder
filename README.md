Run: **python src/synchronization.py --source_path='./source_folder' --replica_path='./replica_folder' --log_path='./logs/synch1.log'  --period=10**
To run: **Ctrl+C**

To test: 
**pip install pytest**
**python -m pytest**

##Running a Python Script in the Background##

**#!/usr/bin/env python3**
**chmod +x test.py**

ignoring hangup signals.
**nohup src/synchronization.py &**
To stop the script:
**ps ax | grep synchronization.py**
**kill PID**
