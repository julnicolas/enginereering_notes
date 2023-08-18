-- Shows how to create tables with usual constraints
-- A many-to-many relationship has been chosen to illustrate
-- the example
-- The uuid extension must be enabled

CREATE TABLE products (
    product_no uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name text NOT NULL,
    price numeric NOT NULL CHECK (price > 0)
);

CREATE TABLE orders (
    order_id uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    shipping_address text NOT NULL
);

CREATE TABLE order_items (
	-- old syntax - 'REFERENCES products(product_no)'
	--
	-- RESTRICT do not allow products to be deleted if they are
	-- references in this table
    product_no uuid REFERENCES products ON DELETE RESTRICT,
	-- if an order is deleted then all references in this table
	-- will be deleted
    order_id uuid REFERENCES orders ON DELETE CASCADE,
    quantity integer,
    PRIMARY KEY (product_no, order_id)
);

/* Please find below some useful insight from postgres' documentation
on row constraints on DELETE events. Please do also mind that UPDATE
events can also be constrained.

Restricting and cascading deletes are the two most common options.
RESTRICT prevents deletion of a referenced row. NO ACTION 
means that if any referencing rows still exist when the 
constraint is checked, an error is raised; this 
is the default behavior if you do not specify anything.
(The essential difference between these two choices is 
that NO ACTION allows the check to be deferred until 
later in the transaction, whereas RESTRICT does not.) 
CASCADE specifies that when a referenced row is deleted, 
row(s) referencing it should be automatically deleted 
as well. There are two other options: SET 
NULL and SET DEFAULT. These cause the referencing column
(s) in the referencing row(s) 
to be set to nulls or their default values, 
respectively, when the referenced row is deleted. Note 
that these do not excuse you from observing any constraints.
For example, if an action specifies SET DEFAULT 
but the default value would not satisfy the foreign key 
constraint, the operation will fail.

*/
