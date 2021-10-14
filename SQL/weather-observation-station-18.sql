set @a = (select min(LAT_N) from STATION);
set @b = (select min(LONG_W) from STATION);
set @c = (select max(LAT_N) from STATION);
set @d = (select max(LONG_W) from STATION);

select round(abs(@a - @c) + abs(@b - @d), 4);