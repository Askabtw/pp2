import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="010205eb"
    )
cur = connection.cursor()

#1
func1 = """
CREATE OR REPLACE FUNCTION search_by_pattern(pname VARCHAR, psurname VARCHAR, pnumber VARCHAR)
RETURNS TABLE(n VARCHAR,
			s VARCHAR,
			num VARCHAR)
			LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT * FROM phonebook 
	WHERE name LIKE '%' || pname || '%'
	AND surname LIKE '%' || psurname || '%'
	AND number LIKE '%' || pnumber || '%';
END
$$;
"""
name = 'Name'
surname = ''
number = ''
cur.execute(func1)
cur.execute(f"SELECT * FROM search_by_pattern('{name}','{surname}', '{number}')")
print("\n#1")
print(cur.fetchall())
#2

proc1 = """
CREATE OR REPLACE PROCEDURE insert_or_update(n VARCHAR, s VARCHAR, num VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE
	cnt INT;
BEGIN
	cnt = COUNT(name) from phonebook WHERE name = n;
	IF cnt = 0 THEN
		INSERT INTO phonebook (name, surname, number) VALUES (n, s, num);
	ELSE
		UPDATE phonebook SET number = num WHERE name = n;
	END IF;
END;
$$;	"""

print("\n#2")
cur.execute(proc1)
cur.execute("CALL insert_or_update('Max', 'Maxim', '13579');")
cur.execute("CALL insert_or_update('Max', 'Maxim', '02468');")
cur.execute("SELECT * FROM phonebook ORDER BY name")
print(cur.fetchall())

#3
proc2 = """
CREATE OR REPLACE PROCEDURE insert_from_list(names VARCHAR ARRAY, surnames VARCHAR ARRAY, numbers VARCHAR ARRAY, len INT)
LANGUAGE plpgsql
AS $$
DECLARE
	cnt INT = 1;
BEGIN
	FOR cnt IN 1..len
	LOOP
		INSERT INTO phonebook (name, surname, number) VALUES (names[cnt], surnames[cnt], numbers[cnt]);
	END LOOP;
END;
$$;"""

print("\n#3")
cur.execute(proc2)
cur.execute("""CALL insert_from_list(
    ARRAY['Dan', 'Pan', 'Tan'],
    ARRAY['Dak', 'Pak', 'Tak'], 
    ARRAY['123', '456', '789'], 
    3);""")
cur.execute("SELECT * FROM phonebook;")
print(cur.fetchall())


#4
#add order by
func2 = """
CREATE OR REPLACE FUNCTION pagination(lim INT, setoff INT)
RETURNS SETOF PhoneBook 
LANGUAGE plpgsql
AS $$
BEGIN
	RETURN QUERY
	SELECT * FROM phonebook
	LIMIT lim OFFSET setoff; 
END;
$$;	"""
cur.execute(func2)
cur.execute("SELECT * FROM pagination(4, 2);")
print("\n#4")
print(cur.fetchall())

#5
proc3 = """
CREATE OR REPLACE PROCEDURE deleting(n VARCHAR, num VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
	DELETE FROM phonebook
	WHERE name = n OR number = num;
END;
$$;"""
cur.execute(proc3)
print("\n#5")
cur.execute(f"CALL deleting('Max', '15136')")
cur.execute("SELECT * FROM phonebook")
print(cur.fetchall())



cur.execute("DROP PROCEDURE insert_from_list;")
cur.execute("DROP PROCEDURE deleting;")
cur.execute("DROP FUNCTION search_by_pattern;")
cur.execute("DROP FUNCTION pagination;")
cur.execute("DROP PROCEDURE insert_or_update;")


connection.commit()
cur.close()
connection.close()