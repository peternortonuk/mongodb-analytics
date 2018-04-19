
def uri(version='3.4'):

    # copy the uri from atlas and select the driver version
    raw_uri_dict = {'3.4': r'mongodb://analytics:<PASSWORD>@mflix-shard-00-00-heksn.mongodb.net:27017,mflix-shard-00-01-heksn.mongodb.net:27017,mflix-shard-00-02-heksn.mongodb.net:27017/test?ssl=true&replicaSet=mflix-shard-0&authSource=admin',
                    '3.6': r'mongodb+srv://analytics:<PASSWORD>@mflix-heksn.mongodb.net/test',
                    'local': r'mongodb://localhost:27017',
                    'student': r'mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin',
                    }
    raw_uri = raw_uri_dict[version]

    # update the password
    password = r'analytics-password'
    password_placeholder = '<PASSWORD>'
    uri = raw_uri.replace(password_placeholder, password)

    return uri
