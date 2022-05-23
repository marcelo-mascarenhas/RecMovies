import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Skeleton from '@mui/material/Skeleton';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { popularMovies } from "../services/movies/popularMovies";
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'
import MoviesList from '../components/movieList';

const urlPostBase = 'https://image.tmdb.org/t/p/original'

export default function Popular() {

  const [movies, setMovies] = React.useState({});
  const loading = true
  
  async function getPopularMovies(farm_id) {
    try {
      const popularMoviesResponse = await popularMovies(farm_id);
      return popularMoviesResponse
    } catch (err) {
      console.log("Error fetching movies");
    }
  }

  React.useEffect(() => {
    getPopularMovies().then((data) => {
      setMovies(data);
      console.log(movies)
    });
  }, []);

  // console.log(Object.values(movies).map((filme, index) => (filme)))

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Container sx={{ py: 3 }} maxWidth="md">
      <Paper>
        <Typography sx={{ py: 1, mb:3 }} align='center' variant="h6">
          Popular
        </Typography>
      </Paper>
      <MoviesList movies={movies}></MoviesList>
    </Container>
    </Box>
  );
}