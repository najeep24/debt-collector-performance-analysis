import pandas as pd
import sqlite3
import os

def csv_to_db(file_path, db_path='debt_collection.db', table_name='debt_data'):
    """Import CSV data into SQLite database"""
    try:
        # Create connection to database
        conn = sqlite3.connect(db_path)
        
        # Read CSV file
        df = pd.read_csv(file_path)
        
        # Write to database
        df.to_sql(table_name, conn, if_exists='append', index=False)
        
        # Close connection
        conn.close()
        
        return True
    except Exception as e:
        print(f"Error importing data: {e}")
        return False

def get_db_stats(db_path='debt_collection.db'):
    """Get basic statistics from the database"""
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Count total records
        cursor.execute("SELECT COUNT(*) FROM debt_data")
        total_records = cursor.fetchone()[0]
        
        # Get average recovery rate
        cursor.execute("SELECT AVG(total_debt_payment_recieved / total_debt * 100) FROM debt_data WHERE total_debt > 0")
        avg_recovery = cursor.fetchone()[0]
        
        # Get average RPC rate
        cursor.execute("SELECT AVG(contact_connected / total_contact * 100) FROM debt_data WHERE total_contact > 0")
        avg_rpc = cursor.fetchone()[0]
        
        # Get average PTP rate
        cursor.execute("SELECT AVG(call_to_ptp / contact_connected * 100) FROM debt_data WHERE contact_connected > 0")
        avg_ptp = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            'total_records': total_records,
            'avg_recovery': avg_recovery,
            'avg_rpc': avg_rpc,
            'avg_ptp': avg_ptp
        }
    except Exception as e:
        print(f"Error getting stats: {e}")
        return None