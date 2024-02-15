-- lists all genres in the database hbtn_0d_tvshows_rate by their rating
-- list all rows in db linked to rows in another database
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN shows_genres ON tv_genres.id = shows_genres.genre_id
JOIN shows ON shows_genres.show_id = shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
