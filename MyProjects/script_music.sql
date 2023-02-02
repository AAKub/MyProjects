create table if not exists Category(
	id_category serial primary key,
	category_name varchar(40) not null
);

create table if not exists Author(
	id_author serial primary key,
	author_name varchar(40) not null
);

create table if not exists CategoryAuthor(
	id_category integer references Category(id_category),
	id_author integer references Author(id_author),
	constraint pk_category_author primary key(id_category, id_author)
);

create table if not exists Album(
	id_album serial primary key,
	album_name varchar(40) not null,
	album_year integer
);

create table if not exists AuthorAlbum(
	id_author integer references Author(id_author),
	id_album integer references Album(id_album),
	constraint pk_author_album primary key(id_author, id_album)
);

create table if not exists Track(
	id_track serial primary key,
	track_name varchar(80) not null,
	track_duration time,
	id_album integer references Album(id_album)
);

create table if not exists Collection(
	id_collection serial primary key,
	collection_name varchar(40) not null,
	collection_year integer
);

create table if not exists TrackCollection(
	id_track integer references Track(id_track),
	id_collection integer references Collection(id_collection),
	constraint pk_track_collection primary key(id_track, id_collection)	
);

