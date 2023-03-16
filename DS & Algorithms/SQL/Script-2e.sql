/* Naći film koji je makar jednom projektovan u svakom bioskopu. */
SELECT
	f.naslov as naslov,
	count(distinct b.BID) as broj_bioskopi
FROM
	film f
	inner join projekcija p on p.FID = f.FID
	inner join bioskop b on b.BID=p.BID 
group by 
	naslov
having	broj_bioskopi = (
					select 
						count(distinct b.BID)
					from 
						bioskop b 
						inner join projekcija p2 on p2.BID=b.BID
					) 
;