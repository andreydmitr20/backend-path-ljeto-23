/* Odrediti u kom bioskopu se nalazi najposjećenija sala. Napomena: najposjećenija sala je
ona u kojoj je bio najveći broj gledalaca, gledano ukupno po svim projekcijama u njoj.*/
SELECT 
	(
	SELECT 
		b.ime
	from
		bioskop b
	where 
		b.BID=BID
	) as bioskop,
	broj_sala,
	broj_gledalaca
FROM
	(	
	SELECT 
		 p.BID as BID,
		 p.broj_sala as broj_sala,
		 sum(p.broj_gledalaca) as broj_gledalaca
	from
		projekcija p 
	group by
		p.BID,
		p.broj_sala
	order BY 
		broj_gledalaca DESC
	LIMIT
		1
	)
;