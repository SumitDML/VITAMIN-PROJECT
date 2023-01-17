INSERT INTO tabs (tab_id,name, display_name) VALUES (1,'Supplements','Supplements');
INSERT INTO tabs (tab_id,name, display_name) VALUES (2,'Nutrients','Nutrients');
INSERT INTO tabs (tab_id,name, display_name) VALUES (3,'Vitamin_D','Vitamin D');

INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (1,'Zones','Zones',3);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (2,'Sunshine_Availability','Sunshine Availability',3);

INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (3,1);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (3,2);