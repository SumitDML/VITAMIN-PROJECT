INSERT INTO tabs (tab_id,name, display_name) VALUES (4,'Spices','Spices');
INSERT INTO tabs (tab_id,name, display_name) VALUES (5,'Common_Food_Allergy','Common Food Allergy');
INSERT INTO tabs (tab_id,name, display_name) VALUES (6,'Spoonacular','Spoonacular');
INSERT INTO tabs (tab_id,name, display_name) VALUES (7,'Edamam','Edamam');
INSERT INTO tabs (tab_id,name, display_name) VALUES (8,'Airnow','Airnow');
INSERT INTO tabs (tab_id,name, display_name) VALUES (9,'USDA Food Nutrition','USDA Food Nutrition');



INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (3,'Spices','Spices',4);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (4,'Common_Food_Allergy','Common Food Allergy',5);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (5,'Spoonacular','Spoonacular',6);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (6,'Edamam','Edamam',7);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (7,'Airnow','Airnow',8);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (8,'USDA Food Nutrition','USDA Food Nutrition',9);


INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (4,3);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (5,4);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (6,5);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (7,6);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (8,7);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (9,8);

