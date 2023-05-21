import { Box, Container, Paper, Typography, ImageList, ImageListItem, IconButton, Grid } from '@mui/material';
import * as React from 'react';
import { useLocation } from 'react-router-dom';
import noPoster from '../../assets/noPoster.jpg'
import FavoriteIcon from '@mui/icons-material/Favorite';
import { getMovieInfo, getMovieRecommender } from "../../services/movies/getMovie";
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import MoviesList from '../../components/movieList';

const urlPostBase = 'https://image.tmdb.org/t/p/original'

export const setMovieFavorite = (favorites, movie) => {
  // Caso esteja no objeto coloca deleta, caso não esteja adiciona
  if (movie)
    favorites[movie.id] ? delete favorites[movie.id] : favorites[movie.id] = movie
  return favorites
} 

export const Movie = () => {

  const location = useLocation();
  const [movie, setMovie] = React.useState({});
  const [movies, setMovies] = React.useState({});

  const [isFavorite, setIsFavorite] = React.useState(false)
  
  const setMovieFavoriteInLocalStorage = (movie) => {

    var favorites = localStorage.getItem('movieRec-movies')
    var favorites_object = JSON.parse(favorites) || {}
    var new_favorites = setMovieFavorite(favorites_object, movie)
    localStorage.setItem('movieRec-movies', JSON.stringify(new_favorites))
  } 

  const handleSetMovieIsFavorite = (movie) => {
    setIsFavorite(!isFavorite)
    setMovieFavoriteInLocalStorage(movie)
  };

  React.useEffect(() => {
    var movie = location.state.movie
    var x = JSON.parse(localStorage.getItem('movieRec-movies')) || {}
    setIsFavorite(x[movie.id])
    setMovie(movie)
    setMovies({})

  }, [location.state]);



  React.useEffect(() => {
    let movie = location.state.movie
    const getMovies = async () => {
      try{
        let movies = await getMovieRecommender(movie.id)
        setMovies(movies)
      }
      catch(err){
        console.log("fail api")
      }
    }
    getMovies();

  }, [location.state]);

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Container sx={{ py: 3 }} maxWidth="lg">
        {Object.keys(movie).length &&
        <Paper sx={{ display: 'flex' }}>
          <Box sx={{ maxWidth: 400, padding:'2%', overflow: 'hidden', }}>
          <ImageList variant="woven" cols={1} gap={0} sx={{borderRadius: 3}}>
              <ImageListItem>
                {/* <img
                  src={`${item.img}?w=161&fit=crop&auto=format`}
                  srcSet={`${item.img}?w=161&fit=crop&auto=format&dpr=2 2x`}
                  alt={item.title}
                  loading="lazy"
                /> */}
              <img
               src={ movie.poster_path ? urlPostBase + movie.poster_path : noPoster} 
                  alt="Icone de Busca"/>
              </ImageListItem>
          </ImageList>
          </Box>
          <Box sx={{ pl:3, pt:5, pb:5, mr:8, maxWidth: 'md', display:'flex', flexDirection:'column', alignItems:'flex-start' }}> 
            <Box>
              <Grid 
                    // spacing={2}
                    // container
                    display='flex'
                    // direction="row"
                    justifyContent="space-between"
                    alignItems="center"
              >   
                <Grid item xs={8}>
                  <Typography sx={{ py: 1, mb:0 }} variant="h4" display="inline">
                    <b>{movie.title}</b> ({movie.release_date.split('-')[0]})
                  </Typography>
                </Grid>
                <Grid item xs={2} ml={2}>
                  {isFavorite ? 
                  <IconButton 
                    color="secondary" 
                    onClick={ () => {handleSetMovieIsFavorite(movie)}}
                    aria-label="add movie to favorites">
                    <FavoriteIcon fontSize="large" />
                  </IconButton>
                  : 
                  <IconButton 
                    color="secondary" 
                    aria-label="add movie to favorites"
                    onClick={ () => {handleSetMovieIsFavorite(movie)}}>
                    <FavoriteBorderIcon fontSize="large" />
                  </IconButton>
                  }

                </Grid>
              </Grid>

              <Typography sx={{ pb: 1, mb:0 }} align='center' variant="body2" display="inline">
              {movie.release_date} <span>&#8226;</span> ({movie.language.toUpperCase()}) <span>&#8226;</span>
              </Typography> 

              <Typography sx={{ py: 0, mb:0 }} align='center' variant="body2" display="inline" >
              {" " + movie.genres.replaceAll(',',", ")}
              </Typography>
            </Box>
              
            <Box>
              <Typography sx={{  mt: 4}} variant="h6">
              Overview
              </Typography>
              <Typography sx={{ pb: 0, mb:0 }} variant="body2">
              {movie.overview}
              </Typography>
            </Box>
          </Box>
          
        </Paper> }

        <Paper>
        <Typography sx={{ py: 1, my:2 }} align='center' variant="h6">
          Recommendations 
        </Typography>
      </Paper>
      <MoviesList movies={movies} small></MoviesList>
        
    </Container>
    </Box>
  );
}