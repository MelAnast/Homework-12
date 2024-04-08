create schema QA_AUTO;
create table QA_AUTO.car_brands (
id int, 
title varchar (255)
);
create table QA_AUTO.car_models (
id int, 
carBrandId int, 
title varchar (255)
);
create table QA_AUTO.users (
id int, 
firstName varchar (255), 
lastName varchar (255), 
email varchar (255), 
password varchar (255)
);
create table QA_AUTO.cars (
id int, 
userId int, 
carBrandId int, 
carModelId int, 
mileage float, 
initialMilleage float
);