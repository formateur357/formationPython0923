import pytest
# from my_database import connect, disconnect

# @pytest.fixture
# def database_connection():
#     connection = connect()
#     yield connection
#     disconnect(connection)

@pytest.mark.requires_network
# def test_query_data(database_connection):
#     # Utilisez database_connection pour exécuter des tests avec une connexion de base de données.
