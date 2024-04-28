select * from hw_qauto.user_profiles  where name like "am%";
select * from hw_qauto.user_profiles  where name like "%am%";
select * from hw_qauto.user_profiles  where name like "_am%";


select max(totalCost), car_brands.title
from hw_qauto.cars inner join hw_qauto.expenses on cars.id=expenses.carId 
inner join hw_qauto.car_brands on hw_qauto.cars.carBrandId = car_brands.id 
where title="Audi";


select 
count(title) as count_models, 
carBrandId as id_brand 
from hw_qauto.car_models 
group by carBrandId 
having carBrandId=1 or carBrandId=2;


select count(userId) as user_count, 
car_brands.title as car_brand, 
car_models.title as car_model 
from hw_qauto.cars inner join hw_qauto.car_brands on carBrandId=car_brands.id 
inner join hw_qauto.car_models on hw_qauto.cars.carModelId=car_models.id 
group by car_brands.title, car_models.title;


select 
distinct name 
FROM hw_qauto.cars inner join user_profiles 
on hw_qauto.cars.userId=hw_qauto.user_profiles.userId;
