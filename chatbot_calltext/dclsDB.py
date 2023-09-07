import pyodbc

cnn = "DRIVER={SQL Server Native Client 11.0};Server=10.18.208.31;Database=DCLS;UID=fxnDFT;PWD=FoxconnDFT1"

# function to fetch data from azure sql database, table name, raw id, and return title text
def fetch_data(table_name:str, row_id:int, col_name:str):
    conn = pyodbc.connect(cnn)
    cursor = conn.cursor()
    query = f"SELECT * FROM {table_name} WHERE id = ?"

    try:    
      cursor.execute(query, row_id)
      row = cursor.fetchone()

      if row is None:
        return "No data found for the given ID"

      d = getattr(row, col_name)
      return d

    except Exception as e:
      return f"An error occurred: {e}"

    finally:
      cursor.close()
      conn.close()
    



