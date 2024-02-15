-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
   -- Each record should display: tv_genres.name - rating sum
   -- Results must be sorted in descending order by their rating
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
JOIN shows_genres ON tv_genres.id = shows_genres.genre_id
JOIN shows ON shows_genres.show_id = shows.id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;