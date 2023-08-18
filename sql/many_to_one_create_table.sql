-- Shows how to create tables with usual constraints
-- A many-to-one relationship has been chosen to illustrate
-- the example
-- The uuid extension must be enabled

-- An owner can have several cars
-- Several times the same
--
-- If owners are deleted then belongings are deleted
-- along
CREATE TABLE owner (
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
);

CREATE TABLE car (
	-- The id can be seen as a plate nomber
    id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    owner_id REFERENCES owner NOT NULL ON DELETE CASCADE,
	brand VARCHAR(30) NOT NULL,
	model VARCHAR(30) NOT NULL
);

