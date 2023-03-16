/* Naći bioskope koji imaju više od jedne sale. */
SELECT
	b.grad_naziv,
	b.ime as bioskop_ime,
	count(b.ime) as broj_sala_ 
FROM
	sala s
	inner join bioskop b on s.BID=b.BID
GROUP BY 
	b.ime
having
	broj_sala_>1
order BY 
	broj_sala_ DESC
;