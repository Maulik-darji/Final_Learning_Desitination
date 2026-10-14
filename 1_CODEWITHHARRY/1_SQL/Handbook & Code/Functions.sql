-- select min(salary) as min_salary, max(salary) as max_salary from users;
-- select gender, sum(salary) as total from users group by gender;
-- select gender, sum(length(name)) as name_len from users group by gender;
-- select name, concat(LOWER(name), 5677), now() as time, year(dob) as year, month(now()) as month, monthname(now()) as nowmonth, monthname(dob) from users; 
-- select name, datediff(curdate(), dob) as days from users;
-- select name, id, mod(id, 2) as remainder from users;


SELECT name, gender,
IF (gender = 'Female', 'Yes', 'No') AS is_female from users;