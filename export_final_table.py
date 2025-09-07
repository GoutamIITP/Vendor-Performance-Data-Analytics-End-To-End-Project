#!/usr/bin/env python3
"""
Export final_table from SQLite database to CSV for Power BI analysis
"""

import sqlite3
import pandas as pd
import os

def export_final_table_to_csv():
    """Export final_table to CSV file"""
    
    # Database path
    db_path = 'inventory.db'
    csv_path = 'final_table_for_powerbi.csv'
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        print(f"✅ Connected to database: {db_path}")
        
        # Read final_table
        query = "SELECT * FROM final_table"
        df = pd.read_sql(query, conn)
        
        print(f"✅ Data loaded successfully!")
        print(f"📊 Shape: {df.shape}")
        print(f"📋 Columns: {list(df.columns)}")
        
        # Export to CSV
        df.to_csv(csv_path, index=False)
        
        # Get absolute path
        abs_path = os.path.abspath(csv_path)
        
        print(f"✅ Data exported to CSV: {abs_path}")
        print(f"📁 File size: {os.path.getsize(csv_path) / (1024*1024):.2f} MB")
        
        # Show sample data
        print("\n📋 Sample data (first 3 rows):")
        print(df.head(3).to_string())
        
        # Close connection
        conn.close()
        print(f"\n🎉 Export completed! You can now import '{csv_path}' into Power BI")
        
        return abs_path
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    export_final_table_to_csv()
