import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import {useLocation} from 'react-router-dom';
import Skeleton from '@mui/material/Skeleton';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { getMovieInfo } from "../../services/movies/getMovie";
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../../assets/noPoster.jpg'
import SearchMovie from '../../components/searchMovie';
import MoviesList from '../../components/movieList';

const urlPostBase = 'https://image.tmdb.org/t/p/original'

export default function MoviesSearch() {

  const location = useLocation();
  const [movies, setMovies] = React.useState({});

  React.useEffect(() => {
    var word = location.state.value

    async function getMovies(){
      try{
        var movies = await getMovieInfo(word)
        setMovies(movies)
      }
      catch(err){
        console.log("fail api")
      }
    }
    getMovies();
  }, [location.state.value]);

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Container sx={{ py: 3 }} maxWidth="md">
        <SearchMovie/>
        <Paper>
          <Typography sx={{ py: 1, mb:3 }} align='center' variant="h6">
            {Object.keys(movies).length ? 'Search Result' : 'No result  '}
          </Typography>
        </Paper>
        <MoviesList movies={movies}></MoviesList>
    </Container>
    </Box>
  );
}