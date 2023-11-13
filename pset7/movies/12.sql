SELECT
  movies.title
FROM
  movies
  JOIN stars AS stars_jl ON movies.id = stars_jl.movie_id
  JOIN people AS people_jl ON stars_jl.person_id = people_jl.id
  JOIN stars AS stars_bc ON movies.id = stars_bc.movie_id
  JOIN people AS people_bc ON stars_bc.person_id = people_bc.id
WHERE
  people_jl.name = 'Jennifer Lawrence'
  AND people_bc.name = 'Bradley Cooper';
