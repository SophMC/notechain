INSERT INTO hilight
SELECT stars.starid AS starid
FROM stars 
LEFT OUTER JOIN planets ON stars.starid == planets.starid
LEFT OUTER JOIN moons ON planets.planetid == moons.planetid
GROUP BY stars.starid ORDER BY (COUNT(planets.planetid) + COUNT(moons.moonid)) 
DESC
LIMIT 1