/* Naći najveću salu. */
SELECT
	b.grad_naziv,
	b.ime as bioskop_ime,
	s.broj_sala,
	max(s.kapacitet) 
FROM
	sala s
	inner join bioskop b on s.BID=b.BID
;