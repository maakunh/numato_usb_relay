BEGIN TRANSACTION;
INSERT INTO "numato_relays" VALUES (0,'URMC8','Numato Lab',8,'COM3','numato_URMC8_8ch_USB_Relay.jpg');
INSERT INTO "numato_relay_status" VALUES (0,'OFF','none','COM3','2021/09/03 11:40:02');
INSERT INTO "numato_relay_status" VALUES (1,'OFF','GTI 1000W','COM3','2021/09/03 11:40:02');
INSERT INTO "numato_relay_status" VALUES (2,'OFF','GTI 600W-2','COM3','2021/09/03 11:38:03');
INSERT INTO "numato_relay_status" VALUES (3,'OFF','GTI 600W-1','COM3','2021/09/03 11:38:03');
INSERT INTO "numato_relay_status" VALUES (4,'OFF','none','COM3','2021/09/03 11:38:03');
INSERT INTO "numato_relay_status" VALUES (5,'OFF','none','COM3','2021/09/03 11:38:03');
INSERT INTO "numato_relay_status" VALUES (6,'OFF','none','COM3','2021/09/03 11:38:03');
INSERT INTO "numato_relay_status" VALUES (7,'ON','Aqua Lights','COM3','2021/09/03 11:38:03');
COMMIT;
