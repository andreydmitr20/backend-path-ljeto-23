/*   Naći gradove u kojima su prikazani svi filmovi.*/
SELECT 
	grad_naziv_,	
	sum(
		(
		select 
			count(*)
		from
			projekcija p2
			inner join bioskop b2 on b2.BID=p2.BID
		WHERE 
			p2.FID =f_FID AND 
			b2.grad_naziv =grad_naziv_
		)>0
	) as film_prikazan
from
	(
	SELECT 
		b.grad_naziv as grad_naziv_,
		naslov,
		f_FID
	from
		bioskop b,
		(
		select 
	    	distinct f.FID as f_FID,
			f.naslov as naslov
		from 
			film f 
			inner join projekcija p on f.FID = p.FID
		)
	)
group BY 		
	grad_naziv_
having 
	film_prikazan = (
					select 
				    	count(distinct b.BID)
					from 
						bioskop b 
						inner join projekcija p on b.BID = p.BID
					)