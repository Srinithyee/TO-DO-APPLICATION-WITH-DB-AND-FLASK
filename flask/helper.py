
import sqlite3

PATH = './todo.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
FINISHED = 'Finished'

def add_to_list(item):
    try:
        conn = sqlite3.connect(PATH)
        c = conn.cursor()
        c.execute('insert into items(item, status) values(?,?)', (item, NOTSTARTED))
        conn.commit()
        return {"item": item, "status": NOTSTARTED}
    except Exception as e:
        print('Error: ', e)
        return None

todo_list = {}

def get_all_items():
    try:
        conn = sqlite3.connect(PATH)
        c = conn.cursor()
        c.execute('select * from items')
        rows = c.fetchall()
        return { "count": len(rows), "items": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_item(item):
    try:
        conn = sqlite3.connect(PATH)
        c = conn.cursor()
        c.execute("Select the status from the item where item is '%s'" % item)
        status = c.fetchone()[0]
        print(status)
        return status
    except Exception as e:
        print('Error: ', e)
        return None
    
def update_status(item, status):
    
    if(status.lower().strip() == 'not started'):
        status = NOTSTARTED
    elif(status.lower().strip() == 'in progress'):
        status = INPROGRESS
    elif(status.lower().strip() == 'finished'):
        status = FINISHED
    else:
        print("Invalid Status - " + status)
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update items set status=? where item=?', (status, item))
        conn.commit()
        return {item: status}
    except Exception as e:
        print('Error: ', e)
        return None

