# pip install mysql-connector-python
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="cafe"
)
c = mydb.cursor()





def add_order(item_no,bill_id,product_id,qty,price):
    amount = qty*price
    c.execute('INSERT INTO orders (`item_no`, `bill_id`, `product_id`, `qty`, `price`, `amount`) VALUES (%s,%s,%s,%s,%s,%s)',
              (int(item_no),int(bill_id),int(product_id),int(qty),float(price),float(amount)))
    mydb.commit()

def add_bill(bill_id,total_amount,amount_tendered):
    c.execute('INSERT INTO bill (bill_id,ref_no,total_amount,amount_tendered) VALUES (%s,998877665544,%s,%s)',
              (int(bill_id),int(total_amount),int(amount_tendered)))
    mydb.commit()


def view_all_orders(order_id):
    if order_id==0:
        c.execute('SELECT * FROM orders')
    else:
        c.execute('SELECT * FROM orders where bill_id=%s',(int(order_id),))
    data = c.fetchall()
    return data


def view_only_order_ids():
    c.execute('SELECT bill_id FROM orders')
    data = c.fetchall()
    return data


def get_order(order_id,product_id):
    c.execute('SELECT p.name,p.product_id,o.price,o.qty FROM  orders o natural join products p where o.bill_id = %s and o.product_id=%s',(int(order_id),int(product_id)))
    data = c.fetchall()
    return data


def edit_order_data(new_prod_id,new_qty,new_price,prod_id):
    amount=new_qty*new_price
    c.execute("UPDATE orders SET product_id=%s, qty=%s, price=%s, amount=%s WHERE product_id=%s",(int(new_prod_id),int(new_qty),float(new_price),float(amount),int(prodd_id)))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(order_id):
    c.execute('DELETE FROM orders where bill_id = %s',(int(order_id),))
    mydb.commit()
