/* Naći filmove koji su projektovani u svakom bioskopu.*/
select 
	naslov,
	(
	select 
		count(distinct b.BID) 
	from 
		film f 
		inner join projekcija p on f.FID = p.FID
		inner join bioskop b on p.BID = b.BID 
	where
		f.FID =f_FID	
	) as broj_bioskopi
from 
	(
	select 
	    distinct f.FID as f_FID,
	    f.naslov as naslov
	from 
		film f 
		inner join projekcija p on f.FID = p.FID
	)
WHERE 
	broj_bioskopi = (select count(*) from bioskop)
order by 
	naslov
;




