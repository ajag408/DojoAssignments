/*SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE city.city_id = 312*/

/*SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy'*/

/*SELECT film.title, film.description, film.release_year
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
WHERE film_actor.actor_id=5*/


/*SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM customer
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
JOIN store ON customer.store_id = store.store_id
WHERE store.store_id = 1 AND city.city_id IN(1, 42, 312, 459)*/


/*SELECT film.title, film.description, film.release_year, film.rating, film.special_features
FROM film
JOIN film_actor ON film.film_id = film_actor.film_id 
WHERE film.rating = 'G' AND film.special_features LIKE '%Behind the Scenes%' AND film_actor.actor_id = 15 */

/*SELECT actor.first_name, actor.last_name, actor.last_update
FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
WHERE film_actor.film_id = 369*/

/*SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND category.name = 'Drama'*/

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE actor.first_name = 'SANDRA' AND actor.last_name = 'KILMER' AND category.name = 'Action'
