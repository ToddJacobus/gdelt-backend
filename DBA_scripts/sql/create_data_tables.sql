BEGIN;
CREATE TABLE IF NOT EXISTS data.gkg_sources (
	id bigserial,
	gkg_id varchar(50) not null,
	pub_date date not null,
	pub_id int not null,
	source_name varchar(100) not null,
	doc_uri	text not null,
	tone numeric,
	positive_score numeric,
	negative_score numeric,
	polarity numeric,
	activity_ref_density numeric,
	pronoun_ref_density numeric,
	word_count numeric,
	share_image text,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_counts (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	count_type varchar(50) not null,
	count_n int not null,
	object_type text,
	location_type int not null,
	location_name text not null,
	location_country varchar(50),
	location_adm1 varchar(50),
	location_lat numeric,
	location_lon numeric,
	location_feature_id varchar(50) not null,
	geom geometry,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_themes (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	theme varchar(50) not null,
	text_offset int,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_locations (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	location_type int not null,
	location_name text not null,
	location_country varchar(50),
	location_adm1 varchar(50),
	location_lat numeric not null,
	location_lon numeric not null,
	location_feature_id varchar(50) not null,
	geom geometry not null,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_people (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	person_name varchar(50) not null,
	text_offset int,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_orgs (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	org_name varchar(50) not null,
	text_offset int,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_liwc (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	dimension varchar(50) not null,
	word_count int not null,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);

CREATE TABLE IF NOT EXISTS data.gkg_images (
	id bigserial,
	source_id bigint,
	pub_date date not null,
	image_url text not null,
	PRIMARY KEY (id, pub_date)
) PARTITION BY RANGE (pub_date);
COMMIT;