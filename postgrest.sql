CREATE SCHEMA api;

CREATE EXTENSION citext;

CREATE TABLE api.feeds (
  id serial PRIMARY KEY,
  name citext NOT NULL,
  url text NOT NULL,
  priority integer NOT NULL DEFAULT 1,
  hidden boolean NOT NULL DEFAULT false,
  created_at timestamptz NOT NULL DEFAULT now(),
  updated_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE api.posts (
  id serial PRIMARY KEY,
  title text NOT NULL,
  description text NOT NULL,
  feed_id int NOT NULL
    REFERENCES api.feeds ON DELETE CASCADE,
  link text,
  read boolean NOT NULL DEFAULT false
);

CREATE role web_anon nologin;
CREATE role postgrest WITH PASSWORD 'postgrest';
grant web_anon to postgrest;

grant usage on schema api to web_anon;
grant all on api.posts to web_anon;
grant all on api.feeds to web_anon;
grant usage, select on sequence api.feeds_id_seq to web_anon;
grant usage, select on sequence api.posts_id_seq to web_anon;
