/*  Naći grad u kom je održana najposjećenija projekcija nekog filma.*/
	SELECT
		b.grad_naziv,	
		p.FID,
		sum(p.broj_gledalaca) as sum_broj_gledalaca
	FROM
		projekcija p
		inner join bioskop b on b.BID=p.BID
	group by 
		b.grad_naziv,	
		p.FID
	order by
		sum_broj_gledalaca DESC
	LIMIT 
		1
;