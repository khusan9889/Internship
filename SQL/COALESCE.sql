/*The COALESCE function accepts a number of arguments and returns the first non-NULL argument.
 It stops evaluating until it finds the first non-NULL argument
*/

SELECT COALESCE(1,2,3); -- return 1

SELECT COALESCE(NULL,'Not NULL','OK'); -- return Not NULL

SELECT COALESCE(1,1/0); -- return 1



/*SQL COALESCE examples */

CREATE TABLE products (
	ID INT PRIMARY KEY,
	product_name VARCHAR(255) NOT NULL,
	product_summary VARCHAR(255),
	product_description VARCHAR(4000) NOT NULL,
	price NUMERIC (11, 2) NOT NULL,
	discount NUMERIC (11, 2),
	CHECK (net_price >= discount)
);



INSERT INTO products (
	ID,
	product_name,
	product_summary,
	product_description,
	price,
	discount
)
VALUES
	(
		1,
		'McLaren 675LT',
		'Inspired by the McLaren F1 GTR Longtail',
		'Performance is like strikin and the seven-speed dual-clutch gearbox is twice as fast now.',
		349500,
		1000
	),
	(
		2,
		'Rolls-Royce Wraith Coupe',
		NULL,
		'Inspired by the words of Sir Henry Royce, this Rolls-Royce Wraith Coupe is an imperceptible force',
		304000,
		NULL
	),
	(
		3,
		'2016 Lamborghini Aventador Convertible',
		NULL,
		'Based on V12, this superveloce has been developed as the Lamborghini with the sportiest DNA',
		271000,
		500
	);

SELECT * FROM products;
/*see example png*/


/* Using SQL COALESCE for substituting NULL values*/
/* here it fulls empty rows with info from another row(70-73)lines*/
SELECT
	ID,
	product_name,
	COALESCE (
		product_summary,     
		LEFT (product_description, 50)
	) excerpt,
	price,
	discount
FROM
	products;
/*see fill_empty.png*/



/*SQL COALESCE and CASE expression */
/*The COALESCE function is syntactic of the CASE expression. It means that the expression*/
COALESCE(argument1,argument2,argument3);

/*can be rewritten using the following CASE expression:*/

CASE
  WHEN (argument1 IS NOT NULL) THEN argument1
  WHEN (argument2 IS NOT NULL) THEN argument2
  ELSE argument3
END

SELECT 
    id,
    product_name,
    price,
    discount,
    (price - 
      CASE
        WHEN discount IS NOT NULL THEN discount
        ELSE 0
    END) AS net_price
FROM
    products;