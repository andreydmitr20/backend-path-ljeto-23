/*  Izlistati parove filmova koji su projektovani u istim salama. */
SELECT 
 	/*p1.FID,*/
 	f1.naslov,
 	/*p2.FID,*/
 	f2.naslov,
 	p1.BID ,
 	p1.broj_sala 
FROM 
 	projekcija p1
 	inner join film f1 on f1.FID=p1.FID,
 	projekcija p2
 	inner join film f2 on f2.FID=p2.FID
where
 	p1.BID = p2.BID and 
 	p1.broj_sala =p2.broj_sala AND
	p1.FID<p2.FID 
group BY 
	p1.FID,
 	p2.FID,
 	p1.BID ,
 	p1.broj_sala 
order BY 
	p1.BID,
	p1.broj_sala