import sqlalchemy as db

PG_USERNAME = 'postgres'
PG_PASSWORD = 'password'
PG_HOST = 'postgres'
DB_NAME = 'nfl'


def connect_to_db():
    """Connect to a db with the given connection string

    Example usage:
        conn_str = db.get_connection_string()
        conn = db.connect_to_db(conn_str)
        results = conn.execute('select col1, col2 from database')

    :param connection_string: database connection string
    :type connection_string: str
    :return: sqlalchemy database engine
    :rtype: sqlalchemy.engine.base.Engine | sqlalchemy.engine.base.Connection
    """
    connection_string = _get_connection_string()
    return db.create_engine(connection_string)


def _get_connection_string():
    return f"postgresql://{PG_USERNAME}:{PG_PASSWORD}@{PG_HOST}/{DB_NAME}"