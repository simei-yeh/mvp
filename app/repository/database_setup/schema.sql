-- postgres database creation

DROP DATABASE IF EXISTS tradetheta

CREATE DATABASE tradetheta

-- ---
-- Table 'stocks'
--
-- ---

create SCHEMA IF NOT EXISTS vol;

DROP TABLE IF EXISTS vol.stocks;

CREATE TABLE vol.stocks (
  stockCode varchar NOT NULL PRIMARY KEY,
  t timestamp default CURRENT_TIMESTAMP,
  symbol text,
  data json NOT NULL,
  pricefactor int NOT NULL,
  volumefactor int NOT NULL,
  timePeriod varchar NOT NULL,
  barLength numeric(10),
  bar varchar(10)
)

-- ---
-- Table 'conids' for IBKR API
--
-- ---


DROP TABLE IF EXISTS vol.conid;

CREATE TABLE vol.conid (
  conid int NOT NULL PRIMARY KEY,
  symbol text NOT NULL,
  companyName text NOT NULL,
  opt varchar[] DEFAULT NULL
)


-- ---
-- Table 'options'
--
-- ---

DROP TABLE IF EXISTS vol.options

CREATE TABLE vol.options (
  id int GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  asof_date timestamp NOT NULL,
  stock_ticker text NOT NULL,
  options_ticker char NOT NULL,
  strike int NOT NULL,
  expiration date NOT NULL,
  open NUMERIC(8,2) NOT NULL CONSTRAINT positive_open CHECK (open > 0),
  high NUMERIC(8,2) NOT NULL CONSTRAINT positive_high CHECK (high > 0),
  low NUMERIC(8,2) NOT NULL CONSTRAINT positive_low CHECK (low > 0),
  close NUMERIC(8,2) NOT NULL CONSTRAINT positive_close CHECK (close > 0),
  volume NUMERIC NOT NULL CONSTRAINT positive_volume CHECK (volume >= 0)
)


-- ---
-- Table 'crypto'
--
-- ---

DROP TABLE IF EXISTS vol.crypto

CREATE TABLE vol.crypto (
  id int GENERATED AlWAYS AS IDENTITY PRIMARY KEY,
  time timestamp,
  asset_id_base char(20) NOT NULL,
  asset_id_quote char(20) NOT NULL,
  rate NUMERIC(30, 10) NOT NULL CONSTRAINT positive_rate CHECK (rate >= 0)
)



-- ---
-- Table 'wsb'
--
-- ---

DROP TABLE IF EXISTS vol.wsb

CREATE TABLE vol.wsb (
  created float DEFAULT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP),
  rankCode text NOT NULL PRIMARY KEY,
  name text NOT NULL,
  ticker text NOT NULL,
  weighted_score float not null,
  score int NOT NULL,
  ups int NOT NULL,
  upvote_ratio float NOT NULL,
  num_comments int NOT NULL
)

