import * as React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { Paper } from '@mui/material';
import MoviesList from '../components/movieList';

export default function Favorites() {

  const [movies, setMovies] = React.useState(JSON.parse(localStorage.getItem('movieRec-movies')) || {});

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Container sx={{ py: 3 }} maxWidth="md">
      <Paper>
        <Typography sx={{ py: 1, mb:3 }} align='center' variant="h6">
            Favorite movies
        </Typography>
      </Paper>
      <MoviesList small movies={movies}></MoviesList>
    </Container>
    </Box>
  );
}