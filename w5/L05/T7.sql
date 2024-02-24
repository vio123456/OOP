SELECT f.name, f.vitamin, f.value
FROM fruits f
WHERE NOT EXISTS (
    SELECT 1
    FROM fruits sub
    WHERE sub.name = f.name AND sub.vitamin = 'Folate (folic acid)'
)
ORDER BY f.name DESC, f.vitamin ASC;
.mode csv
.headers on
.import --csv  t4_product.csv product