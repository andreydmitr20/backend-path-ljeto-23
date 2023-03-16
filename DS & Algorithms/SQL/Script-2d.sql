/* Naći bioskope u kojima je svaka projekcija imala više od 50 gledalaca. */
SELECT
	distinct b.BID as b_BID,
	b.ime as bioskop_ime
FROM
	projekcija p 
	inner join bioskop b on p.BID=b.BID
WHERE 
	not exists (
		select 
		    p.BID
		from 
		 	projekcija p 
		WHERE 
			p.BID=b_BID AND 
			p.broj_gledalaca <= 50
	)
;