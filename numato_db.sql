BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "numato_relays" (
	"id"	INTEGER,
	"device_name"	STRING,
	"supplyer"	STRING,
	"relay_nums"	INTEGER,
	"port"	STRING,
	"diagram_pic"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "numato_relay_status" (
	"relay_num"	INTEGER,
	"status"	STRING,
	"name"	STRING,
	"port"	STRING,
	"date"	STRING,
	PRIMARY KEY("relay_num")
);
CREATE TABLE IF NOT EXISTS "numato_relay_operation_history" (
	"datetime"	TEXT,
	"port"	TEXT,
	"relaynum"	TEXT,
	"operation"	TEXT
);
COMMIT;
