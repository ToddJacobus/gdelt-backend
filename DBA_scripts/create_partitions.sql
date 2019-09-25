
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m1
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m2
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m3
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m4
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m5
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m6
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m7
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m8
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m9
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m10
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m11
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_sources_yr2018m12
                        PARTITION OF data.gkg_sources
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m1
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m2
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m3
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m4
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m5
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m6
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m7
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m8
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m9
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m10
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m11
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_counts_yr2018m12
                        PARTITION OF data.gkg_counts
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m1
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m2
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m3
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m4
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m5
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m6
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m7
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m8
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m9
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m10
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m11
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_images_yr2018m12
                        PARTITION OF data.gkg_images
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m1
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m2
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m3
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m4
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m5
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m6
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m7
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m8
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m9
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m10
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m11
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_liwc_yr2018m12
                        PARTITION OF data.gkg_liwc
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m1
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m2
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m3
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m4
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m5
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m6
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m7
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m8
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m9
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m10
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m11
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_locations_yr2018m12
                        PARTITION OF data.gkg_locations
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m1
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m2
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m3
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m4
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m5
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m6
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m7
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m8
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m9
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m10
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m11
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_orgs_yr2018m12
                        PARTITION OF data.gkg_orgs
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m1
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m2
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m3
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m4
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m5
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m6
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m7
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m8
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m9
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m10
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m11
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_people_yr2018m12
                        PARTITION OF data.gkg_people
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m1
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-1-01') TO ('2018-2-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m2
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-2-01') TO ('2018-3-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m3
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-3-01') TO ('2018-4-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m4
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-4-01') TO ('2018-5-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m5
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-5-01') TO ('2018-6-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m6
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-6-01') TO ('2018-7-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m7
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-7-01') TO ('2018-8-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m8
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-8-01') TO ('2018-9-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m9
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-9-01') TO ('2018-10-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m10
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-10-01') TO ('2018-11-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m11
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-11-01') TO ('2018-12-01');
                 
                    CREATE TABLE IF NOT EXISTS data.gkg_themes_yr2018m12
                        PARTITION OF data.gkg_themes
                            FOR VALUES FROM ('2018-12-01') TO ('2019-01-01');
                