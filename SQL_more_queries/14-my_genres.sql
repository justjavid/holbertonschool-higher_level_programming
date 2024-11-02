-- listing all genres of the show Dexter
SELECT g.name name FROM (tv_show_genres sg INNER JOIN tv_genres g ON sg.genre_id = g.id) 
INNER JOIN tv_shows s ON s.id = sg.show_id
WHERE s.title = 'Dexter' ORDER BY g.name;
