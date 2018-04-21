# coursera
#### https://www.coursera.org/learn/introduction-mongodb
#### https://www.coursera.org/learn/introduction-mongodb/supplement/OwBDM/setting-up-your-course-environment

## set up conda environment
#### >> conda create --name intro-to-mongodb
#### activate the environment
#### >> activate intro-to-mongodb
#### then install the following
#### >> conda install python=3.6
#### >> conda install pymongo dnspython jupyter matplotlib
#### if within an enterprise then go to external channel
#### >> conda install foo -c defaults
#### then for mflix project
#### >> conda install Flask==0.12.2
#### >> conda install Flask-Login==0.4.0
#### and stupid question that requires python 2.7 means create a new new environment as follows, from root:
#### >> conda create -n intro-to-mongodb27 python=2.7 anaconda
#### >> activate intro-to-mongodb27
#### >> conda install pymongo dnspython jupyter matplotlib basemap

## set up git hub repository
#### C:\dev\code\mongodb-analytics
#### so clone from root with
#### >> git clone https://github.com/peternortonuk/mongodb-analytics.git

## install mongodb enterprise
#### https://www.mongodb.com/download-center#enterprise
#### add this location to 'system environment variable' PATH 
#### C:\Program Files\MongoDB\Server\\{version}\bin
#### apply to 'system' not 'user' path variable and make it highest priority
#### test by running at the command prompts
#### >> mongo --nodb
#### >> quit()
#### confirm version installed
#### >> pip freeze | grep pymongo
#### >> pymongo==3.6.1
#### note the following binaries:
#### mongod.exe = server; mongo.exe = client

## set up mongodb environment
#### mongodb is installed as part of enterprise but in order to use local database then:
#### https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
#### set up the mongodb environment ie create data directory
#### C:\data\db

## set up atlas
#### https://www.mongodb.com/cloud/atlas
#### login: peternorton99@yahoo.com.au
#### cluster name: mflix
#### cluster user: analytics
#### cluster password: analytics-password

## test connection to atlas
#### >> ping mflix-shard-00-01-heksn.mongodb.net
#### >> telnet mflix-shard-00-01-heksn.mongodb.net 27017

## connect to atlas using local mongodb server
#### from here: C:\Program Files\MongoDB\Server\\{version}\bin
#### start the local mongo db server
#### >> mongod
#### confirm the version
#### >> mongo --version
#### copy the uri from atlas and modify password placeholder, then test the connection
#### >> mongo "uri" --ssl --authenticationDatabase admin --username analytics --password analytics-password

## import data from csv
#### go to location of file. here we're using this file: movies_initial.csv
### import into atlas:
#### >> mongoimport --type csv --headerline --db mflix --collection movies_initial --host "<CLUSTER>/<SEED_LIST>" --authenticationDatabase admin --ssl --username analytics --password analytics-password --file movies_initial.csv
### import into local db:
#### >> mongoimport --db mflix --collection movies_initial --type csv --file movies_initial.csv --headerline
#### >> mongoimport --db cleansing --collection people-raw --file people-raw.json

## set up compass
#### https://www.mongodb.com/download-center?jmp=nav#compass
#### go to db and get the connection string; return to compass and connect to host
#### for example, connect to atlas or localdb
#### GOTCHA: if you get error message topology destroyed; then just restart the connection
####    the database does persist after server is closed

## start jupyter notebook
#### from this folder
#### C:\dev\code\mongodb-analytics\intro-to-mongodb\notebooks
#### start a jupyter notebook server
#### >> jupyter notebook
#### then interact with notebook here
#### http://localhost:8888/
#### if folder isnt visible then specify as follows (use double quotes)
#### jupyter notebook --notebook-dir "C:\dev\code\mongodb-analytics\intro-to-mongodb\notebooks"

