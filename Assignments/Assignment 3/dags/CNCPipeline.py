from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
#import processing

def Preprocessing_to_Snowflake():
    import pandas as pd
    import numpy as np
    import snowflake.connector as sf
    import pandas as pd
    import numpy as np
    pd.set_option('display.max_columns', 100)
    from snowflake.connector.pandas_tools import write_pandas
    from pandas import DataFrame
    import h5py
    import glob

    print("Libraries Installed")

    # Combining all the 18 Experiment Files and Generating a frame that will be uploaded as a Snowflake Table
    path = r'./archive' # use your path
    all_files = glob.glob(path + "/*.csv")

    li = []

    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df['file_name'] = filename
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True)
    frame.reset_index(drop=True, inplace=True)
    frame["file_name"] = frame.file_name.str[-17:]
    frame['Exp_No'] = (frame.file_name.str[-6:].str[:2]).astype(int)
    frame.Machining_Process.value_counts()

    frame.columns = frame.columns.str.upper()
    print("All DataFrames Combined")


    print("Establishing Snowflake Connection")
    ## SnowFlake Connection

    ctx = sf.connect(
    user = 'jayshilj',
    password = 'Admin1234',
    account = 'ri58064.us-east-2.aws',
    warehouse = 'compute_wh',
    database = 'CNC_MILL_TOOL_WEAR',
    schema = 'PUBLIC'
    )
    cs = ctx.cursor()

    cs.execute('''USE CNC_MILL_TOOL_WEAR''')

    # Creating the CNC Table in Snowflake with all the column names
    cs.execute('''CREATE OR REPLACE TABLE EXPERIMENT(
        X1_ActualPosition NUMBER,
        X1_ActualVelocity NUMBER,
        X1_ActualAcceleration NUMBER,
        X1_CommandPosition NUMBER,
        X1_CommandVelocity NUMBER,
        X1_CommandAcceleration NUMBER,
        X1_CurrentFeedback NUMBER,
        X1_DCBusVoltage NUMBER,
        X1_OutputCurrent NUMBER,
        X1_OutputVoltage NUMBER, 
        X1_OutputPower NUMBER,
        Y1_ActualPosition NUMBER,
        Y1_ActualVelocity NUMBER,
        Y1_ActualAcceleration NUMBER,
        Y1_CommandPosition NUMBER,
        Y1_CommandVelocity NUMBER,
        Y1_CommandAcceleration NUMBER,
        Y1_CurrentFeedback NUMBER,
        Y1_DCBusVoltage NUMBER,
        Y1_OutputCurrent NUMBER,
        Y1_OutputVoltage NUMBER, 
        Y1_OutputPower NUMBER,
        Z1_ActualPosition NUMBER,
        Z1_ActualVelocity NUMBER,
        Z1_ActualAcceleration NUMBER,
        Z1_CommandPosition NUMBER,
        Z1_CommandVelocity NUMBER,
        Z1_CommandAcceleration NUMBER,
        Z1_CurrentFeedback NUMBER,
        Z1_DCBusVoltage NUMBER,
        Z1_OutputCurrent NUMBER,
        Z1_OutputVoltage NUMBER,
        S1_ActualPosition NUMBER,
        S1_ActualVelocity NUMBER,
        S1_ActualAcceleration NUMBER,
        S1_CommandPosition NUMBER,
        S1_CommandVelocity NUMBER,
        S1_CommandAcceleration NUMBER,
        S1_CurrentFeedback NUMBER,
        S1_DCBusVoltage NUMBER,
        S1_OutputCurrent NUMBER,
        S1_OutputVoltage NUMBER,
        S1_OutputPower NUMBER,
        S1_SystemInertia NUMBER,
        M1_CURRENT_PROGRAM_NUMBER NUMBER,
        M1_sequence_number NUMBER,
        M1_CURRENT_FEEDRATE NUMBER,
        Machining_Process varchar(255),
        FILE_NAME varchar(255),
        EXP_NO NUMBER)''')

    write_pandas(ctx, frame, "EXPERIMENT")


    ####################### TRAIN CSV FILE ###############################

    # Extracting the R+Traing Data and Preprocessing t=it
    df_train = pd.read_csv(r'./archive/Train/train.csv') # use your path
    df_train.columns = df_train.columns.str.upper()



    cs.execute('''CREATE OR REPLACE TABLE TRAIN(
        NO NUMBER,
        MATERIAL varchar(255),
        FEEDRATE NUMBER,
        CLAMP_PRESSURE NUMBER,
        TOOL_CONDITION varchar(255),
        MACHINING_FINALIZED varchar(255),
        PASSED_VISUAL_INSPECTION varchar(255))''')

    write_pandas(ctx, df_train, "TRAIN")
    print("Snowflake Tables Gerated")


def Establish_Snowflake_Connection():
    print("Establishing Snowflake Connection")
    ## SnowFlake Connection

def Creating_Tables_in_Snowflake():
    print("Snowflake Tables Created")

def Inserting_CNC_Mill_Data_in_SnowflakeDB():
    print("Snowflake Tables Created")







############################### AIRFLOW PART ####################################
default_args = {
  'owner': 'team3',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'catchup': False,
    'email': ['jayshil97@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}


dag = DAG('CNCPipeline',default_args=default_args,schedule_interval=None,max_active_runs=1)


t1 = BashOperator(
    task_id='Install_All_Libraries',
    bash_command='pip install boto3',
    dag=dag)

t2 = PythonOperator(
    task_id='Preprocessing_to_Snowflake',
    python_callable=Preprocessing_to_Snowflake,
    dag=dag,
)

t3 = PythonOperator(
    task_id='Establish_Snowflake_Connection',
    python_callable=Establish_Snowflake_Connection,
    dag=dag,
)

t4 = PythonOperator(
    task_id='Creating_Tables_in_Snowflake',
    python_callable=Creating_Tables_in_Snowflake,
    dag=dag,
)

t5 = PythonOperator(
    task_id='Inserting_CNC_Mill_Data_in_SnowflakeDB',
    python_callable=Creating_Tables_in_Snowflake,
    dag=dag,
)


t6 = BashOperator(
    task_id='Launch_Fast_API',
    bash_command='pip list',
    dag=dag)

# t2 = BashOperator(
#     task_id='Upload_Raw_Data_to_AWS_S3',
#     bash_command='python /root/EdgarPipeline/dags/Upload_Raw_Data_to_AWS_S3.py',
#     dag=dag)
# t3 = BashOperator(
#     task_id='Preprocess_The_Data',
#     bash_command='python /root/EdgarPipeline/dags/Preprocess_The_Data.py',
#     dag=dag)

# t4 = BashOperator(
#     task_id='Establish_Connection_With_Google_API',
#     bash_command='python /root/EdgarPipeline/dags/Establish_Connection_With_Google_API.py',
#     dag=dag)

# t4 = BashOperator(
#     task_id='MainPreprocessing',
#     bash_command='python /root/EdgarPipeline/dags/processing.py',
#     dag=dag)

# t5 = BashOperator(
#     task_id='Generating_Analytics_Files',
#     bash_command='python /root/EdgarPipeline/dags/Generating_Analytics_Files.py',
#     dag=dag)

# t6 = BashOperator(
#     task_id='Upload_to_AWS_S3',
#     bash_command='python /root/EdgarPipeline/dags/Upload_to_AWS_S3.py',
#     dag=dag)

#python /home/jayshil/PycharmProjects/EdgarPipeline/dags/processing.py

t1 >> [t2 , t3] >> t4 >> t5 >> t6