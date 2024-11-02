--  listing all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT g.name genre, COUNT(sg.show_id) number_of_shows FROM tv_genres g INNER JOIN tv_show_genres sg
ON g.id = sg.genre_id GROUP BY sg.genre_id ORDER BY number_of_shows DESC;
