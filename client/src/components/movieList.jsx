import * as React from 'react';
import Grid from '@mui/material/Grid';
import Skeleton from '@mui/material/Skeleton';
import Typography from '@mui/material/Typography';
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'
import { useNavigate } from "react-router-dom";

const urlPostBase = 'https://image.tmdb.org/t/p/original'

export default function MoviesList(props) {
  const navigateTo = useNavigate()
  return (
    <Grid container spacing={2} justifyContent="center" alignItems="stretch">
    {props.movies && Object.values(props.movies).map((movie, index) => (
        <Grid sx={{height:'100%'}} item key={index} xs={props.small ? 5 : 6 } sm={props.small? 3: 4} md={ props.small ? 2: 3}>
          <CardActionArea>
            <Card key={index}
                onClick={() => {console.log('teste'); navigateTo("/movie", {state:{movie}})} }
                sx={{height:'100%', display: 'flex', flexDirection: 'column' }}
            >
            {/* Image */}
            <CardMedia
                component="img"
                sx={{
                  // 16:9
                  width: '100%',
                }}
                image={ movie.poster_path ? urlPostBase + movie.poster_path : noPoster}
                alt={movie.title}
            />
            {/* Descrição */}
            {movie ? (
                <CardContent sx={{ flexGrow: 1, p: 2}}>
                    <Typography noWrap gutterBottom variant="body2" sx={{ height: '20px'}}>
                        {movie.title}
                    </Typography>
                    <Typography display="block" variant="caption" color="text.secondary">
                        {movie.release_date}
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
  );
}