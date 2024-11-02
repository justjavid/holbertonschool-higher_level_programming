-- listing all genres of the show Dexter
SELECT g.name name FROM tv_show_genres sg INNER JOIN tv_genres g ON sg.genre_id = g.id
WHERE sg.show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter') ORDER BY g.name;
