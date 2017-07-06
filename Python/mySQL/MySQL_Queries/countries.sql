/* SELECT countries.name, languages.language, languages.percentage 
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene'
ORDER BY percentage DESC */

/*SELECT countries.name, COUNT(cities.country_id)
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY cities.country_id
ORDER BY COUNT(cities.country_id) DESC*/

/*SELECT cities.name
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC*/

/*SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC*/


/*SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000*/

/*SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital>200 AND life_expectancy>75*/

/*SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE cities.district = 'Buenos Aires' AND cities.population>500000*/


SELECT region, count(*) AS countries
FROM countries
GROUP BY region
ORDER BY count(*) DESC

