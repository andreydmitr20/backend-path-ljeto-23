select 
	naslov, 
	(select 
		count(distinct b.grad_naziv) 
	from 
		film f 
		inner join projekcija p on f.FID = p.FID
		inner join bioskop b on p.BID = b.BID 
	where
		f.FID =f_FID
	) as grad_broj 
from 
	(
	select 
	    distinct f.FID as f_FID,
		f.naslov as naslov
	from 
		film f 
		inner join projekcija p on f.FID = p.FID
		inner join bioskop b on p.BID = b.BID  
	)
order by naslov
;




