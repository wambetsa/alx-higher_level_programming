-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
   -- The tv_genres table contains only one record where name = Comedy (but the id can be different)
   -- Each record should display: tv_shows.title
   -- Results must be sorted in ascending order by the show title
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT a.title
FROM tv_shows AS a
JOIN tv_show_genres AS b
ON a.id = b.show_id
JOIN tv_genres AS c
ON b.genre_id = c.id
WHERE c.name = 'Comedy'
ORDER BY a.title ASC;