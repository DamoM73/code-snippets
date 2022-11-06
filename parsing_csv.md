```pseudocode
FOR row of csv
	READ row

    IF rating THEN
        IF rating NOT IN rating table THEN
            ADD rating to rating table
        ENDIF
        GET rating_id
    ENDIF

    ADD show details to show table
    GET show_id

    IF director THEN
        FOR director
            IF director NOT IN director table THEN
                ADD director to director table
            ENDIF
            GET director_id
            ADD show_id and director_id to show_director table
        NEXT director
    ENDIF

    IF cast THEN
        FOR actor
            IF actor NOT IN actor table THEN
                ADD actor to actor table
            ENDIF
            GET actor_id
            ADD show_id and actor_id to cast table
        NEXT actor
    ENDIF

    IF country THEN
        FOR country
            IF country NOT IN country table THEN
                ADD country to country table
            ENDIF
            GET country_id
            ADD show_id and country_id to show_country table
        NEXT country
    ENDIF

    FOR category
        IF category NOT IN category table THEN
            ADD category to category table
        ENDIF
        GET category_id
        ADD show_id and category_id to show_category_table
    NEXT category
NEXT row
```

