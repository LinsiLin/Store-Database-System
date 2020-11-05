-- Script name: inserts.sql
-- Author:      Linsi Lin
-- Purpose:     insert sample data to test the integrity of this database system
   
-- the database used to insert the data into.
-- USE StoreDB;
   
-- businessOwner table inserts
   INSERT INTO businessOwner (business_owner_id, email, name,address, phone_number) VALUES 
   (1, 'jedsuperficial@optonline.net', 'John', '58 Middle Point Rd','912-855-8593'),
   (2, 'xanunclescrooge@live.com','XiaMen', '15 Le Conte Ave', '415-856-8482' ), 
   (3, 'patsycuddly@me.com','Mary','1447 Van Dyke Ave','230-452-2241' );

-- company table inserts
INSERT INTO company (company_id, name,email, address, phone) VALUES
(1,'Hawkshield','hawk@gmail.com', '158 San Dyke Ave','250-420-6025'),
(2,'BaolanGem','Bao@gmail.com', '66 Ceres St','520-652-8596'),
(3,'Lanhuachao','Lan@gmail.com', '5118 3rd St','415-523-6699');

-- ownership table inserts
INSERT INTO ownership (ownership_id, company_id, business_owner_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3);

-- department table inserts
INSERT INTO department (department_id, name,phone) VALUES
(1, 'store', '562-854-6052'),
(2, 'warehouse', '562-854-6922'),
(3, 'accounting', '562-204-6920');

-- store table inserts
INSERT INTO store (store_id, address,phone) VALUES
(1, '1102 Barbara St', '415-569-4820'),
(2, '5405 85th Ave', '415-852-4820'),
(3, '320 Peg St', '415-854-8765'),
(4, 'online', '415-524-5615'),
(5, 'online', '241-211-2354'),
(6, 'online', '421-562-1210');


-- warehouse table inserts
INSERT INTO warehouse (warehouse_id, address,phone) VALUES
(1, '3412 5th St', '462-841-8695'),
(2, '3961 6th St', '442-546-4455'),
(3, '3517 7th St', '453-844-6554');

-- composition table inserts
INSERT INTO composition(composition_id,company_id,department_id,store_id,warehouse_id) VALUES
(1,1,1,1,1),
(2,1,2,2,2),
(3,1,3,3,3);

-- person table inserts
INSERT INTO person (SSN, name, email, dob, date_joined, is_supervisor, comapny_id) VALUES
('785125369', 'John', 'Jognh@gmail.com', '1988-05-06', '2005-05-12', 'Yes', 1),
('654323546','Mary', 'Maryk@yahoo.com', '1982-08-03', '2015-06-05', 'No', 1),
('454622455','Michael', 'Mrig@yahoo.com', '1979-05-09', '2019-09-08', 'No', 1),
('421325843','Pete', 'Petenige@concast.com', '1991-08-07', '2018-03-22', 'Yes', 1),
('581145234','Jason', 'Jasonk#yahoo,com', '1992-09-08', '2019-12-05', 'No', 1),
('421513205','Nancy', 'Nancydfa@gmail.com', '1998-05-09', '2019-01-09', 'No', 1),
('432923125', 'Roger', 'Roger@gmail.com', '1992-08-07', '2019-03-02', 'Yes', 1),
('123645326', 'Uyry', 'Uyryin@gmail.com', '1977-05-04', '2000-03-08', 'No', 1),
('982321212', 'Liam', 'LiamLiang@gmail.com', '1988-09-08', '2008-09-12', 'No', 1),
('904135232', 'Paul', 'Paul@yahoo.com', '1999-07-05', '2009-03-07', 'No', 1);

-- dependent table inserts
INSERT INTO dependent (dependent_id, name, address) VALUES
(1, 'Polo', '5755 County Rd #335'),
(2, 'Bill', '38621 Vineland St'),
(3, 'Tencent', '519 W Ponca');


-- relation table inserts
INSERT INTO relation (relationship_id, SSN, dependent_id) VALUES
(1, '785125369', 1),
(2,'654323546', 2),
(3,'454622455', 3);

-- supervisor table inserts
INSERT INTO supervisor (supervisor_id, SSN, name, department_id) VALUES
(1, '785125369', 'John', 1),
(2, '421325843','Pete', 2),
(3,'432923125', 'Roger', 3);


-- regularEmployee table inserts
INSERT INTO regularEmployee (employee_id, SSN, name,  department_id, store_id, warehouse_id) VALUES
(1, '785125369', 'John',  1, 1, null),
(2, '654323546', 'Mary',  1, 2, null),
(3, '454622455', 'Michael',  1, 3, null);


-- manager table inserts
INSERT INTO manager ( manager_id, SSN, name) VALUES
(1,'123645326', 'Uyry'),
(2,'982321212', 'Liam'),
(3,'904135232', 'Paul');

-- management table inserts
INSERT INTO management (management_id, manager_id, department_id, store_id, warehouse_id) VALUES
(1,1, 1,1,1),
(2,2,2,2,2),
(3,3, 3,3,3);

-- supplier table inserts
INSERT INTO supplier (supplier_id, company_name, address) VALUES
(1, 'LuckySupply', 'Fuzhou'),
(2, 'FulaiSupply', 'Guangzhou'),
(3, 'FastSupply', 'Shanghai');

-- logisticProvider table inserts
INSERT INTO logisticProvider (logistic_provider_id, company_name, address, store_id, warehouse_id) VALUES
(1, 'logisticProvider1', '1710 W Madison Ave', 1, null),
(2,'logisticProvider2', '909 E Meadows Ct', 2, null),
(3,'logisticProvide3', '12928 Eagle Ridge Dr', null, 1);


-- request table inserts
INSERT INTO request (request_id, manager_id, supplier_id) VALUES
(1, 1,1),
(2,2,2),
(3,3,3);

-- designate table inserts
INSERT INTO designate (designation_id, supplier_id, logistic_provider_id) VALUES
(1, 1,1),
(2,2,2),
(3,3,3);

-- customer table inserts
INSERT INTO customer (customer_id, email, shipping_address) VALUES
(1, 'hojnh@gmail.com', '2403 College St'),
(2, 'Mrigpaul@yahoo.com', '216 N Farm Cir W'),
(3, 'uyer@yahoo.com', '34 Wyatt Ellis Rd');

-- onlineStore table inserts
INSERT INTO onlineStore (URL, bestseller, store_id) VALUES
('www.store1.com', 'camera1', 4),
('www.store2.com', 'camera2', 5),
('www.store3.com', 'camera3', 6);

-- loginAccount table inserts
INSERT INTO loginAccount (account_id, customer_id, URL) VALUES
(1,1,'www.store1.com'),
(2,2, 'www.store2.com'),
(3,3, 'www.store3.com');


-- checkOut table inserts
INSERT INTO checkOut (check_out_id,  total, quantity) VALUES
(1, 20.02, 3),
(2, 500.18, 8),
(3, 60, 5);

-- products table inserts
INSERT INTO products (product_id, product_name, product_SKU, check_out_id) VALUES
(1, 'Camera1', 'BURS123D',1),
(2,'Camera2','FADF502D', 2),
(3,'Camera3', 'DFAD212E', 3);

-- orderProduct table inserts
INSERT INTO orderProduct (order_id, product_id, customer_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3);

 
-- shoppingCart table inserts
INSERT INTO shoppingCart ( cart_id, tax, date_added, warehouse_id) VALUES
(1, 12, '2020-05-08', 1),
(2, 5, '2020-06-07', 1),
(3, 6, '2020-06-07', 1);

-- contain table inserts
INSERT INTO contain (contain_id, product_id, cart_id, date_added) VALUES
(1, 1, 1, '2020-05-08'),
(2, 2, 2, '2020-06-07'),
(3, 3, 3, '2020-06-07');

-- paymentType table inserts
INSERT INTO paymentType( payment_type_id, name, address) VALUES
(1, 'creditCard', '5645 State 73 Hwy'),
(2,'bankAccount', '610 S 2nd Ave'),
(3, 'only two', '532 25th ave');

-- billingInfo table inserts
INSERT INTO billingInfo ( billing_id, customer_id, payment_type_id, amount) VALUES
(1,1,1,20.02),
(2,2,1,500.18),
(3,3,2,60);

-- creditCard table inserts
INSERT INTO creditCard ( card_number, payment_type_id, expiration_date, cvv, bank) VALUES
(11, 1, '2020-09-08', '565', 'BOA'),
(22, 1, '2020-09-04', '531', 'FRB'),
(33, 1, '2020-07-04', '123', 'PNC');

-- bankAccount table inserts
INSERT INTO bankAccount ( account_number, payment_type_id, bank, rounting_number) VALUES
(1, 2, 'BOA', 1243),
(2,2, 'FRB', 1513),
(3,2, 'PNC', 2653);

-- shippingCompany table inserts
INSERT INTO shippingCompany ( shipping_company_id, phone_number, name) VALUES
(1, '212-532-5632', 'Ship1'),
(2, '561-523-2313', 'Ship2'),
(3, '412-5632-5263', 'Ship3');


-- arrangement table inserts
INSERT INTO arrangement( arrangement_id, warehouse_id, shipping_company_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3);

-- delivery table inserts
INSERT INTO delivery( delivery_id, shipping_company_id, customer_id, delivery_date) VALUES
(1,1,1, '2018-08-01'),
(2,2,2, '2020-08-12'),
(3,3,3, '2018-09-03');

-- brickmortarStore table inserts
INSERT INTO brickmortarStore ( bm_id, store_id, address, name) VALUES
(1, 1,'1102 Barbara St', 'BMStore1'),
(2, 2,'5405 85th Ave','BMStore2'),
(3,3,'320 Peg St','BMStore3');


-- storage table inserts
INSERT INTO storage ( storage_id, bm_id, product_id, product_SKU) VALUES
(1, 1, 1, 'BURS123D'),
(2,2,2,'FADF502D'),
(3,3,3,'DFAD212E');


-- creditBureau table inserts
INSERT INTO creditBureau ( credit_bureau_id, name, address) VALUES
(1, 'CB1','138 Stetson Rd'),
(2,'CB2', '6810 Dahlonega Hwy'),
(3,'CB3', '7069 Harder Rd');

-- creditVerification table inserts
INSERT INTO creditVerification ( verification_id, check_out_id, credit_bureau_id) VALUES
(1,1,1),
(2,2,2),
(3,3,3);

-- image table inserts
INSERT INTO image( image_id, size, image_path, product_id) VALUES
(1, 1, 'wwww.image1.com', 1),
(2,1,'wwww.image2.com', 2),
(3,1,'wwww.image3.com', 3);

-- review table inserts
INSERT INTO review(  review_id, review_date, review_by, product_id) VALUES
(1, '2019-05-09', 'Xiar', 1),
(2, '2020-06-08', 'Paul', 2),
(3, '2020-06-08', 'Snow', 3);

-- productSpecification table inserts
INSERT INTO productSpecification( specs_id, model, name, product_id) VALUES
(1, 'M1', 'MCamera',1),
(2,'M2', 'HCamera',2),
(3,'M3', 'OCamera',3);

-- supervision table inserts
INSERT INTO supervision( SSN, supervision_id) VALUES
('654323546',1),
('454622455',2),
('581145234',3);

