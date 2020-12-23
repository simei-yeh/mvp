-- postgres database creation

DROP DATABASE IF EXISTS tradetheta

CREATE DATABASE tradetheta

-- ---
-- Table 'stonks'
--
-- ---

create SCHEMA IF NOT EXISTS vol;

DROP TABLE IF EXISTS vol.stocks;

CREATE TABLE vol.stocks (
  asof_date timestamp,
  ticker text,
  open NUMERIC(8,2) NOT NULL CONSTRAINT positive_open CHECK (open > 0),
  high NUMERIC(8,2) NOT NULL CONSTRAINT positive_high CHECK (high > 0),
  low NUMERIC(8,2) NOT NULL CONSTRAINT positive_low CHECK (low > 0),
  close NUMERIC(8,2) NOT NULL CONSTRAINT positive_close CHECK (close > 0),
  volume NUMERIC NOT NULL CONSTRAINT positive_volume CHECK (volume >= 0),
  interval NUMERIC NOT NULL,
  -- PRIMARY KEY (listings_id)
)


-- ---
-- Table 'options'
--
-- ---

DROP TABLE IF EXISTS vol.options

CREATE TABLE vol.options (
  asof_date timestamp NOT NULL,
  stock_ticker text NOT NULL,
  options_ticker char NOT NULL,
  strike int NOT NULL,
  expiration date NOT NULL,
  open NUMERIC(8,2) NOT NULL CONSTRAINT positive_open CHECK (open > 0),
  high NUMERIC(8,2) NOT NULL CONSTRAINT positive_high CHECK (high > 0),
  low NUMERIC(8,2) NOT NULL CONSTRAINT positive_low CHECK (low > 0),
  close NUMERIC(8,2) NOT NULL CONSTRAINT positive_close CHECK (close > 0),
  volume NUMERIC NOT NULL CONSTRAINT positive_volume CHECK (volume >= 0),
  -- PRIMARY KEY (users_id)
)


-- ---
-- Table 'crypto'
--
-- ---

DROP TABLE IF EXISTS vol.crypto

CREATE TABLE vol.crypto (
  asof_date timestamp,
  asset_id_base char NOT NULL,
  asset_id_quote char NOT NULL,
  rate NUMERIC(16, 10) NOT NULL CONSTRAINT positive_rate CHECK (rate > 0).
  PRIMARY KEY (bookings_id)
)



-- ---
-- Table 'wsb'
--
-- ---

DROP TABLE IF EXISTS vol.wsb

CREATE TABLE vol.wsb (
  asof_date timestamp,
  stock_ticker text NOT NULL,
  options_ticker char NULL,
  indicator_bullish boolean,
  indicator_bearish boolean,
  karma int NOT NULL,
  popularity int NOT NULL,
  comments int NOT NULL,
  -- PRIMARY KEY (bookings_id)
)

-- CONSTRAINT fk_listings references herkbath.listings(id) ON DELETE CASCADE
--CONSTRAINT fk_listings references herkbath.listings(id)
-- CONSTRAINT fk_users references herkbath.users(id)
-- ---
-- Foreign Keys
-- ---
-- ---
-- Table Properties
-- ---

-- ALTER TABLE listings ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE bookings ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE users ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO listings (id,dailyPrice,weeklyDiscount,monthlyDiscount,max_guests,min_stay,max_stay) VALUES
-- ('','','','','','','');
-- INSERT INTO bookings (id,checkin,checkout,adults,children,infants,id_listings,id_users) VALUES
-- ('','','','','','','','');
-- INSERT INTO users (id,username) VALUES
-- ('','');