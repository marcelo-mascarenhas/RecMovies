import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import {useLocation} from 'react-router-dom';
import Skeleton from '@mui/material/Skeleton';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'

const urlPostBase = 'https://image.tmdb.org/t/p/original'


export default function Movies() {
  
  const location = useLocation();
  const [loadings, setLoadings] = React.useState({});
  const loading = true

  
  if (location.state){
    var movies = location.state.moviesInfos
    console.log(movies)
  }

  // console.log(Object.values(movies).map((filme, index) => (filme)))

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Container sx={{ py: 3 }} maxWidth="md">
      <Paper>
        <Typography sx={{ py: 1, mb:3 }} align='center' variant="h6">
          Search Results
        </Typography>
      </Paper>
      
        <Grid container spacing={2} justifyContent="center" alignItems="stretch">
        {Object.values(movies).map((filme, index) => (
            <Grid sx={{height:'100%'}} item key={index} xs={6} sm={4} md={3}>
              <CardActionArea>
                <Card
                    sx={{height:'100%', display: 'flex', flexDirection: 'column' }}
                >
                {/* Image */}
                {loading ? (
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