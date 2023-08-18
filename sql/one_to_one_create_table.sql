-- Shows how to create tables with usual constraints
-- A one-to-one relationship has been chosen to illustrate
-- the example
-- The uuid extension must be enabled

-- A person has one unique name, if a person is deleted,
-- the corresponding name must be deleted too.
CREATE TABLE people (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
);

-- This would be the same as adding name to people
CREATE TABLE names (
    people_id REFERENCES people ON DELETE CASCADE,
	name VARCHAR(30),
	PRIMARY KEY(people_id, name)
);

