insert into author(author_name)
values 
	('Элвис Пресли'),
	('The Beatles'),
	('Джо Сатриани'),
	('Фрэнк Заппа'),
	('Led Zeppelin'),
	('Deep Purple'),
	('Iron Maiden'),
	('Armin van Buuren'),
	('David Guetta'),
	('Skrillex');
	
insert into category(category_name)
values
	('рок-н-ролл'),
	('инструментальный рок'),
	('хард-рок'),
	('хаус'),
	('дабстеп'),
	('транс');
	
insert into categoryauthor(id_category, id_author)
values
	(1,1),
	(1,2),
	(2,3),
	(2,4),
	(2,5),
	(3,6),
	(4,7),
	(4,8),
	(5,9),
	(6,10);

insert into album(album_name, album_year)
values
	('Just a Little More Love', 2002),
	('Guetta Blaster', 2004),
	('Recess', 2014),
	('Make It Bun Dem', 2012),
	('How the West Was Won', 2003),
	('The Song Remains the Same', 1976),
	('Who Do We Think We Are', 1976),
	('Embrace', 2015),
	('One Love', 2009),
	('Make It Bun Dem', 2012);


insert into authoralbum(id_author, id_album)
values
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	(6,6),
	(7,7),
	(8,8),
	(9,9),
	(10,10);

insert into track(track_name, track_duration, id_album)
values
	('Just a Little More Love', '00:03:20', 1),
	('Love Dont Let Me Go', '00:03:36', 1),
	('Money', '00:03:06', 2),
	('Stay', '00:03:30', 2),
	('Movement Girl', '00:04:01', 2),
	('Ease My Mind', '00:05:02', 3),
	('Make It Bun Dem', '00:04:34', 4),
	('Bring It On Home', '00:04:21', 5),
	('What Is and What Should Never Be', '00:04:41', 5),
	('Dancing Days', '00:03:42', 5),
	('Stairway to Heaven', '00:09:38', 5),
	('Since Ive Been Loving You', '00:08:02', 5),
	('Heartbreaker', '00:07:25', 5),
	('The Song Remains the Same', '00:06:00', 6),
	('Stairway to Heaven', '00:10:58', 6),
	('Misty Mountain Hop', '00:04:43', 6);

insert into collection(collection_name, collection_year)
values
	('THE HEARTBREAK HOTEL', 2022),
	('ROCK SONGS HITS OF MARCH', 2016),
	('THE DIGITAL HOURGLASS', 2011),
	('REBEL ROCK BOX NOVEMBER SONGS', 2021),
	('ROCK LEGENDS 70S', 2008),
	('ROCK HITS 150', 2021),
	('100 FM HITS 70S', 2011),
	('ELECTRIC UNIVERSE - TIMELESS', 2021);
	
insert into trackcollection(id_track, id_collection)
values
	(1,1),
	(2,1),
	(3,1),
	(4,2),
	(5,3),
	(6,3),
	(7,4),
	(8,4),
	(9,4),
	(10,5),
	(11,5),
	(12,6),
	(13,6),
	(14,7),
	(15,7),
	(16,8);
	

