--1--
select
	album_name,
	album_year
from
	album
where
	album_year = 2018;
--2--	

select
	track_name,
	track_duration
from
	track
order by
	track_duration desc
limit 1;

--3--
select
	track_name
from
	track
where
	track_duration >= '00:03:30';
--4--	
select
	collection_name
from
	collection
where
	collection_year between 2018 and 2020;
	
--5--
select
	author_name
from
	author
where
	author_name not like '% %';

	--6--
select
	track_name
from
	track
where
	lower(track_name) like '% my %'or
	lower(track_name) like '% my'or
	lower(track_name) like 'my %';
