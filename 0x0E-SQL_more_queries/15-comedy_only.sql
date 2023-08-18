-- Script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT ts.title
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE tg.name = "Comedy"
ORDER BY ts.title ASC;