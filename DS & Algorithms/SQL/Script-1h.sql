/*  Naći film koji je u svakoj sali projektovan bar 2 puta.*/
/* TODO */
	SELECT
		f.naslov,	
		p.BID,
		p.broj_sala,
		p.FID as FID,
		count(*) as projektovan	
	FROM
		projekcija p
		inner join film f on f.FID=p.FID
	group BY 
		p.BID,
		p.broj_sala,
		p.FID
	HAVING 
		projektovan>=2
	;