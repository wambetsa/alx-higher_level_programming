-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
   -- The tv_shows table contains only one record where title = Dexter (but the id can be different)
   -- Each record should display: tv_genres.name
   -- Results must be sorted in ascending order by the genre name
   -- You can use only one SELECT statement
   -- The database name will be passed as an argument of the mysql command

SELECT a.name AS name
FROM tv_genres AS a
JOIN tv_show_genres AS b
ON b.genre_id = a.id
JOIN tv_shows AS c
ON b.show_id = c.id
WHERE c.title = 'Dexter'
ORDER BY a.name ASC;