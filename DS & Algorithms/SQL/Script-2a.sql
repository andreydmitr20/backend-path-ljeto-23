/* Naći sale koje imaju kapacitet veći od 50 mjesta. */
SELECT
	b.grad_naziv,
	b.ime as bioskop_ime,
	s.broj_sala,
	s.kapacitet 
FROM
	sala s
	inner join bioskop b on s.BID=b.BID
WHERE 
	s.kapacitet > 50
;