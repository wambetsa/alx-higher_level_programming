-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
   -- Each record should display: tv_shows.title - tv_show_genres.genre_id
   -- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT a.title, b.genre_id
FROM tv_shows AS a, tv_show_genres AS b
WHERE b.show_id = a.id
ORDER BY a.title ASC, b.genre_id ASC;