# Import the required libraries
import streamlit as st
from cassandra.cluster import Cluster


def connect_to_cassandra():
    cluster = Cluster(['localhost'], port=9042)  # Replace 'localhost' with your Cassandra host address and '9042' with the appropriate port
    session = cluster.connect('zuhaib')  # Replace 'your_keyspace' with your actual Cassandra keyspace name
    return session

def fetch_data(session):
    query = "SELECT * FROM student;"  # Replace 'your_table' with the actual table name in your keyspace
    rows = session.execute(query)
    return rows


def main():
    st.title('Cassandra Connector Streamlit App')

    # Connect to Cassandra
    session = connect_to_cassandra()

    # Fetch data from Cassandra
    data = fetch_data(session)

    # Display the data in the Streamlit app
    for row in data:
        st.write(row)

if __name__ == '__main__':
    main()
