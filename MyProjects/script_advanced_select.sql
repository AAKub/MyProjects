--1--
select category_name, count(*) from categoryauthor
join category on categoryauthor.id_category = category.id_category
group by category_name
order by count(*) desc;

--2--
select count(*) from track
join album on track.id_album = album.id_album
where album.album_year between 2019 and 2020;

--3--
select album_name, avg(track_duration) from track
join album on track.id_album = album.id_album
group by album_name
order by avg;

--4--
select author_name from authoralbum
join author on authoralbum.id_author = author.id_author
join album on authoralbum.id_album = album.id_album
where album_year <> 2020;

--5--
select collection_name from collection
join trackcollection on collection.id_collection = trackcollection.id_collection 
join track on track.id_track = trackcollection.id_track 
join album on track.id_album = album.id_album 
join authoralbum on authoralbum.id_album = album.id_album
join author on authoralbum.id_author = author.id_author
where author.author_name = 'Элвис Пресли'
group by collection_name;

--6--
select album_name, count(*) as number_of_categories from album
join authoralbum using(id_album)
join author using(id_author)
join categoryauthor on categoryauthor.id_author = author.id_author
join category using(id_category)
group by album_name
having count(*) > 1 


--7--
select track_name from track
left join trackcollection using(id_track)
left join collection using(id_collection)
where trackcollection.id_track is null; 

--8--
select author_name, track_duration from author
left join authoralbum using(id_author)
left join album using(id_album)
left join track using(id_album)
where track_duration = (select min(track_duration) from track);

--9--
select distinct album_name from album
left join track using(id_album)
where track.id_album in (
	select id_album from track
	group by id_album
	having count(id_album) = (
		select count(id_album) from track
		group by id_album
		order by count(id_album)
		limit 1
	)
)








