
INSERT INTO tabs (tab_id,name, display_name) VALUES (1,'Vitamin_D','Vitamin D');
INSERT INTO tabs (tab_id,name, display_name) VALUES (2,'Supplements','Supplements');
INSERT INTO tabs (tab_id,name, display_name) VALUES (3,'Nutrients','Nutrients');
INSERT INTO tabs (tab_id,name, display_name) VALUES (4,'Spices','Spices');
INSERT INTO tabs (tab_id,name, display_name) VALUES (5,'Common_Food_Allergies','Common Food Allergies');
INSERT INTO tabs (tab_id,name, display_name) VALUES (6,'Restaurants','Restaurants');
INSERT INTO tabs (tab_id,name, display_name) VALUES (7,'Recipes','Recipes');
INSERT INTO tabs (tab_id,name, display_name) VALUES (8,'Pollution','Pollution');
INSERT INTO tabs (tab_id,name, display_name) VALUES (9,'Food Nutrition','Food Nutrition');



INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (1,'Zones','Zones',1);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (2,'Sunshine_Availability','Sunshine Availability',1);

INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (3,'Supplements','Supplements',2);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (4,'Nutrients','Nutrients',3);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (5,'Spices','Spices',4);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (6,'Common_Food_Allergies','Common Food Allergies',5);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (7,'Restaurants','Restaurants',6);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (8,'Recipes','Recipes',7);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (9,'Pollution','Pollution',8);
INSERT INTO tab_childs (tab_child_id,name, display_name,tab_id) VALUES (10,'Food Nutrition','Food Nutrition',9);



INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,1);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (1,2);

INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (2,3);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (3,4);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (4,5);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (5,6);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (6,7);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (7,8);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (8,9);
INSERT INTO tab_child_mappings (tab_id,tab_child_id) VALUES (9,10);

