import * as React from 'react';
import Grid from '@mui/material/Grid';
import Skeleton from '@mui/material/Skeleton';
import Typography from '@mui/material/Typography';
import { Card, CardActionArea, CardContent, CardMedia } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'
import { useNavigate } from "react-router-dom";

const urlPostBase = 'https://image.tmdb.org/t/p/original'

function NoMoviesToShow() {
  let rows = [];
  for (let i = 0; i < 6; i++) {
    rows.push(<Skeleton sx={{ width: '100%', my: 2, mx: 1 }} variant="rectangular" width={168} height={315} />);
  }
  return rows;
}

function MovieImage({ movie }) {
  return (<CardMedia
    component="img"
    sx={{
      width: '100%',
    }}
    image={movie.poster_path ? urlPostBase + movie.poster_path : noPoster}
    alt={movie.title}
  />)
}

function MovieDesciption({ movie }) {
  return (
    <CardContent sx={{ flexGrow: 1, p: 2 }}>
      <Typography noWrap gutterBottom variant="body2" sx={{ height: '20px' }}>
        {movie.title}
      </Typography>
      <Typography display="block" variant="caption" color="text.secondary">
        {movie.release_date}
      </Typography>
    </CardContent>)
}

function Movie({ movie }) {
  const navigateTo = useNavigate()
  return (
    <Card key={movie.title + movie.poster_path}
      onClick={() => { navigateTo("/movie", { state: { movie } }) }}
      sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
    >
      <MovieImage movie={movie} />
      <MovieDesciption movie={movie} />
    </Card>
  )
}

export default function MoviesList(props) {
  var xs_ = 6; var sm_ = 4; var md_ = 3
  props.small ? (xs_ = 5, sm_ = 3, md_ = 2) : null

  return (
    <Grid container spacing={2} justifyContent="center" alignItems="stretch">
      {Object.keys(props.movies).length ?
        (Object.values(props.movies).map((movie, index) => (
          <Grid sx={{ height: '100%' }} item key={index} xs={xs_} sm={sm_} md={md_}>
            <CardActionArea>
              <Movie movie={movie} />
            </CardActionArea>
          </Grid>
        )))
        :
        <NoMoviesToShow />
      }
    </Grid>
  );
}