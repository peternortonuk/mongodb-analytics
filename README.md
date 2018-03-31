# coursera
#### https://www.coursera.org/learn/introduction-mongodb
#### https://www.coursera.org/learn/introduction-mongodb/supplement/OwBDM/setting-up-your-course-environment

## set up conda environment
#### >> conda create --name intro-to-mongodb
#### activate the environment
#### >> activate intro-to-mongodb
#### then install
#### >> conda install python=3.6
#### >> pip install pymongo dnspython

## set up git hub repository
#### C:\dev\code\mongodb-analytics
#### with the folder structure
####     └── intro-to-mongodb
####        ├── mflix
####        └── notebooks

## install mongodb enterprise
#### https://www.mongodb.com/download-center#enterprise
#### shell is here:
#### C:\Program Files\MongoDB\Server\3.6\bin\mongo.exe
#### database server is here:
#### C:\Program Files\MongoDB\Server\3.6\bin\mongod.exe
#### add this location to 'system environment variable' PATH 
#### apply to 'system' not 'user' path variable and make it highest priority
#### so copy this: C:\Program Files\MongoDB\Server\3.6\bin;
#### test my running at the command prompts
#### >> mongo --nodb
#### >> quit()

## set up atlas
#### https://www.mongodb.com/cloud/atlas
#### login: peternorton99@yahoo.com.au
#### cluster name: mflix
#### cluster user: analytics
#### cluster password: analytics-password

## start jupyter notebook
#### from this folder
#### C:\dev\code\mongodb-analytics\intro-to-mongodb\notebooks
#### start a jupyter notebook server
#### >> jupyter notebook
#### then interact with notebook here
#### http://localhost:8888/
#### if folder isnt visible then specify as follows (use double quotes)
#### jupyter notebook --notebook-dir "C:\dev\code\mongodb-analytics\intro-to-mongodb\notebooks"

