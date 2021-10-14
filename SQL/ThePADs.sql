select concat(name, '(', substr(Occupation, 1, 1), ')') 
from OCCUPATIONS
order by name;

select concat("There are a total of ", count(Occupation), " ", lower(Occupation), "s.")
from OCCUPATIONS
group by occupation
order by count(Occupation);