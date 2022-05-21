import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Skeleton from '@mui/material/Skeleton';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { popularMovies } from "../services/movies/popularMovies";
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'

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
      
        <Grid container spacing={2} justifyContent="center" alignItems="stretch">
        { movies && Object.values(movies).map((filme, index) => (
            <Grid sx={{height:'100%'}} item key={index} xs={6} sm={4} md={3}>
              <CardActionArea>
                <Card
                    sx={{height:'100%', display: 'flex', flexDirection: 'column' }}
                >
                {/* Image */}
                {filme ? (
                    <CardMedia
                        component="img"
                        sx={{
                          // 16:9
                          width: '100%',
                        }}
                        image={ filme.poster_path ? urlPostBase + filme.poster_path : noPoster}
                        alt={filme.title}
                      />
                    ) : (
                      <Skeleton variant="rectangular" height='100px' />
                )}

                {/* Descrição */}
                {filme ? (
                    <CardContent sx={{ flexGrow: 1, p: 2}}>
                        <Typography noWrap gutterBottom variant="body2" sx={{ height: '20px'}}>
                            {filme.title}
                        </Typography>
                        <Typography display="block" variant="caption" color="text.secondary">
                            {filme.release_date}
                        </Typography>
                    </CardContent>
                    ) : (
                    <CardContent sx={{ flexGrow: 1, p: 2}}>
                        <Skeleton />
                        <Skeleton width="30%" />
                    </CardContent>
                )}

                </Card>
              </CardActionArea>
            </Grid>
        ))}
        </Grid>
    </Container>
    </Box>
  );
}