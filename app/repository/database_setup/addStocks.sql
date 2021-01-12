CREATE OR REPLACE PROCEDURE add_stocks(
	stock_data json
)
AS $$
DECLARE
	stock_id varchar;
BEGIN
	-- insert into the stocks table
	INSERT INTO vol.stocks SELECT * from json_populate_record(NULL::vol.stocks,stock_data) ON CONFLICT (stockcode) DO UPDATE SET(data) = (SELECT data FROM json_populate_record (NULL::vol.stocks,stock_data ))

  RETURNING stockcode INTO stock_id;

END;
$$
LANGUAGE PLPGSQL;