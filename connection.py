import clickhouse_connect
from clickhouse_connect.driver import httputil

# Define connection parameters
insight_host = '10.10.3.66'
username = 'nithindidigam'
password = '66zDxmXc'
port = 8123
big_pool_mgr = httputil.get_pool_manager(maxsize=30, num_pools=20)

# Function to create a new ClickHouse client
def create_client():
    return clickhouse_connect.get_client(
        host=insight_host,
        username=username,
        password=password,
        port=port,
        query_limit=10000000000,
        connect_timeout='100000',
        send_receive_timeout='300000',
        settings={
            'max_insert_threads': 32,
            'max_query_size': 10000000000,
            'receive_timeout': 0,
            'max_memory_usage': 1017374182400
        },
        pool_mgr=big_pool_mgr
    )

# Create a ClickHouse client
client = create_client()

# Export the client as Client
Client = client

