/*  Naći gradove u kojima se prikazivao film koji je do sada imao najveći broj projekcija. */
select 
	distinct b.grad_naziv
from 
	(
	select 
		f_FID,
		max(broj_projekcija)
	from (
		select 
			f_FID,
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
		) 
	) m
	inner join projekcija p on m.f_FID = p.FID
	inner join bioskop b on p.BID = b.BID
;




