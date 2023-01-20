
INSERT INTO tabs (tab_id,name, display_name) VALUES (1,'Vitamin_D','Vitamin D');
INSERT INTO tabs (tab_id,name, display_name) VALUES (2,'Supplements','Supplements');
INSERT INTO tabs (tab_id,name, display_name) VALUES (3,'Nutrients','Nutrients');


INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (1,'Zones','Zones',1);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (2,'Sunshine_Availability','Sunshine Availability',1);

INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,1);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,2);