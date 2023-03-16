/*  Naći film koji je u svakoj sali projektovan bar 2 puta.*/
SELECT 
	naslov_ as film,
	sum(
		(
		select 
			count(*) 
		from
			projekcija p 
		WHERE 
			p.FID = FID_ AND 
			p.BID = BID_ AND 
			p.broj_sala = broj_sala_
		)>=2
	   ) as prikazan_u_sale
from (
		SELECT
			s.BID as BID_,
			s.broj_sala	as broj_sala_,
			f.naslov as naslov_,
			f.FID as FID_
		FROM
			sala s,
			film f	
	)	
group by 
	naslov_
having 
	prikazan_u_sale = (
		SELECT 
			count(*)
		from
			sala 
			)
;