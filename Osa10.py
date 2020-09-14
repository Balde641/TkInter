def delete():
    conn = sqlte3.connet("tasklist.db")

    c = conn.cursor

    c.execute("DELETE FROMtaska WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close