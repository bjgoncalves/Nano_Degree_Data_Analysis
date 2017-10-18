## EXTRACTING THE DATA by Beltino Goncalves

/*
This query is to identify my closest city.
*/

SELECT * 
FROM city_list
WHERE country in '%United States%' AND city like '%New York%'


/*
This query is to identify the average temperaty for each city
*/

SELECT * 
	FROM city_data
	WHERE city LIKE '%New York%'

/*
This query is to identify the average global temperatures by year
*/

SELECT * 
	FROM global_data

/*
This query gets  Average temperature from Local Munich, Germany 
*/

SELECT * 
	FROM city_data
	WHERE city LIKE '%Munich%' 


