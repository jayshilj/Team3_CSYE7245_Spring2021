## TFX Airflow
#### Lab 7 Airflow tfx

1. Google Docs Link: https://docs.google.com/document/d/1hUkyf5xo1fJJzFPbH9cUKZ2AtX83ExkLmnQc7rYuwZ8/edit#heading=h.n7oilkyeazln

2. CLAT Document Link: https://codelabs-preview.appspot.com/?file_id=1hUkyf5xo1fJJzFPbH9cUKZ2AtX83ExkLmnQc7rYuwZ8#1


From https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop <br>
Codebase available here: https://github.com/tensorflow/tfx/tree/master/tfx/examples/airflow_workshop


### Getting Started 

Clone the contents of this repository. Alternatively, you may clone the example directly from the [TFX Git Repo](https://github.com/tensorflow/tfx).

Create a Python 3.7 Virtual environment. The `setup_demo.sh` contains all the required dependencies. Install the dependencies by running:

```
sh setup_demo.sh
```

This should take a while to install all dependencies.


#### Starting Airflow

Start the Airflow server in daemon
```
airflow webserver -D
```
Start the Airflow Scheduler
```
airflow scheduler
```

Once both are running - you should be able to access the Airflow UI by visiting http://127.0.0.1:8080/home on your browser.

To kill the Airflow webserver daemon:
```
lsof -i tcp:8080  
```
You should see a list of all processes that looks like this:
```
COMMAND   PID        USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
Python  13280 dileepholla    6u  IPv4 0x8f7b5be5240cda23      0t0  TCP *:http-alt (LISTEN)
Python  13325 dileepholla    6u  IPv4 0x8f7b5be5240cda23      0t0  TCP *:http-alt (LISTEN)
Python  13362 dileepholla    6u  IPv4 0x8f7b5be5240cda23      0t0  TCP *:http-alt (LISTEN)
Python  13401 dileepholla    6u  IPv4 0x8f7b5be5240cda23      0t0  TCP *:http-alt (LISTEN)
Python  13431 dileepholla    6u  IPv4 0x8f7b5be5240cda23      0t0  TCP *:http-alt (LISTEN)
```

Kill the process by running `kill <PID>` - in this case, it would be `kill 13280`

### Usage Instructions

All usage instructions and complete step-by-step tutorial is available [here.](https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop)

### References & Citation

[TensorFlow TFX Workshp](https://www.tensorflow.org/tfx/tutorials/tfx/airflow_workshop) <br>
[TFX on GitHub](https://github.com/tensorflow/tfx)