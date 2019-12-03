CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs AS d, sizes AS s WHERE s.min < d.height and d.height <= s.max;

-- All dogs with parents ordered by decreASing height of their parent
CREATE TABLE by_parent_height AS
  SELECT child FROM parents AS a, dogs AS b WHERE a.parent = b.name ORDER BY -b.height;

-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT a.child AS one, b.child AS two FROM parents AS a, parents AS b WHERE a.parent = b.parent and a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT one || " and " || two || " are " || a.size || " siblings" FROM siblings, size_of_dogs AS a, size_of_dogs AS b WHERE one = a.name and two = b.name and a.size = b.size;

-- Ways to stack 4 dogs to a height of at leASt 170, ordered by total height
CREATE TABLE stacks_helper(dogs, stack_height, lASt_height);

-- Add your INSERT INTOs here
INSERT INTO stacks_helper
  select name, height, height FROM dogs;

INSERT INTO stacks_helper
  select a.dogs || ", " || b.name, a.stack_height + b.height, b.height FROM stacks_helper AS a, dogs AS b WHERE b.height > a.lASt_height;

INSERT INTO stacks_helper
  select a.dogs || ", " || b.name, a.stack_height + b.height, b.height FROM stacks_helper AS a, dogs AS b WHERE b.height > a.lASt_height;

INSERT INTO stacks_helper
  select a.dogs || ", " || b.name, a.stack_height + b.height, b.height FROM stacks_helper AS a, dogs AS b WHERE b.height > a.lASt_height;

CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE stack_height >= 170 ORDER BY stack_height;
