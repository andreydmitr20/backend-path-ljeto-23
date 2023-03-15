/* Naći film koji je imao najveći broj projekcija.*/
select 
	naslov,
	(select 
		count(*) 
	from 
		projekcija p 
	where
		p.FID =f_FID
	) as broj_projekcija
from 
	(
	select 
	    distinct f.FID as f_FID,
		f.naslov as naslov
	from 
		film f 
		inner join projekcija p on f.FID = p.FID
	)
order by 
	broj_projekcija DESC
LIMIT 
	1
;




