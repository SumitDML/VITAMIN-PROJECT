INSERT INTO tabs (tab_id,name, display_name) VALUES (4,'Common_Food_Allergy','Common Food Allergy');
INSERT INTO tabs (tab_id,name, display_name) VALUES (5,'Spices','Spices');


INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (3,'Common_Food_Allergy','Common Food Allergy',4);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (4,'Spices','Spices',5);

INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (4,3);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (5,4);