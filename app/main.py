from app.db import Base
from app.api import Server

if __name__ == '__main__':
    server = Server()
    server.run()
    # for table_name in Base.metadata.tables.keys():
    #     print(table_name)

    print('Start')