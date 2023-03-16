/*  Naći parove FID, BID tako da je film sa ključem FID bar 3 puta 
prikazan u bioskopu sa ključem BID. */
SELECT
	p.FID as FID,
	p.BID as BID,
	count(*) as broj_projekcija
FROM
	projekcija p
group by 
	p.FID,p.BID  
HAVING 
	broj_projekcija>=3
;