#!/usr/bin/env python3
import os
import time
import sys
import psycopg2
from psycopg2 import OperationalError

def wait_for_db():
    """Wait for database to be available"""
    print("Waiting for PostgreSQL to be ready...")
    
    db_config = {
        'host': os.environ.get('POSTGRES_HOST', 'db'),
        'port': os.environ.get('POSTGRES_PORT', '5432'),
        'user': os.environ.get('POSTGRES_USER', 'aikademiya'),
        'password': os.environ.get('POSTGRES_PASSWORD', 'aikademiya'),
        'database': os.environ.get('POSTGRES_DB', 'aikademiya'),
    }
    
    max_retries = 3
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            print(f"Attempt {retry_count + 1}/{max_retries}: Connecting to PostgreSQL...")
            conn = psycopg2.connect(**db_config)
            conn.close()
            print("✅ PostgreSQL is ready!")
            return True
        except OperationalError as e:
            print(f"❌ PostgreSQL not ready yet: {e}")
            retry_count += 1
            if retry_count < max_retries:
                time.sleep(2)
    
    print("❌ Failed to connect to PostgreSQL after all retries")
    return False

if __name__ == "__main__":
    if wait_for_db():
        sys.exit(0)
    else:
        sys.exit(1)