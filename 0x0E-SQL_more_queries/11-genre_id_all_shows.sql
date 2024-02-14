--Import the database dump of hbtn_0d_tvshows to your MySQL server: download (same as 10-genre_id_by_show.sql)
--Write a script that lists all shows contained in the database hbtn_0d_tvshows
SELECT a.title, b.genre_id
FROM tv_shows AS a
LEFT JOIN tv_show_genres AS b
ON a.id = b.show_id
ORDER BY a.title ASC, b.genre_id ASC;