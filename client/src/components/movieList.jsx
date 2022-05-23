import * as React from 'react';
import Grid from '@mui/material/Grid';
import Skeleton from '@mui/material/Skeleton';
import Typography from '@mui/material/Typography';
import { Card, CardActionArea, CardContent, CardMedia, Paper } from '@mui/material';
import noPoster from '../assets/noPoster.jpg'
import { useNavigate } from "react-router-dom";

const urlPostBase = 'https://image.tmdb.org/t/p/original'

export default function MoviesList(props) {

  console.log('movielist', props.movies)
  console.log(Object.values(props.movies).map((movie, index) => (console.log(movie))))

  const navigateTo = useNavigate()
  return (
    <Grid container spacing={2} justifyContent="center" alignItems="stretch">
    {Object.keys(props.movies).length? (Object.values(props.movies).map((movieRec, index) => (
        <Grid sx={{height:'100%'}} item key={index} xs={props.small ? 5 : 6 } sm={props.small? 3: 4} md={ props.small ? 2: 3}>
          <CardActionArea>
            <Card key={index}
                onClick={() => {console.log('teste'); navigateTo("/movieRec", {state:{movieRec}})} }
                sx={{height:'100%', display: 'flex', flexDirection: 'column' }}
            >
            {/* Image */}
            <CardMedia
                component="img"
                sx={{
                  // 16:9
                  width: '100%',
                }}
                image={ movieRec.poster_path ? urlPostBase + movieRec.poster_path : noPoster}
                alt={movieRec.title}
            />
            {/* Descrição */}
                <CardContent sx={{ flexGrow: 1, p: 2}}>
                    <Typography noWrap gutterBottom variant="body2" sx={{ height: '20px'}}>
                        {movieRec.title}
                    </Typography>
                    <Typography display="block" variant="caption" color="text.secondary">
                        {movieRec.release_date}
                    </Typography>
                </CardContent>
            </Card>
          </CardActionArea>
        </Grid>
    )))
    :
    <>
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    <Skeleton sx={{width: '100%', my: 2, mx: 1}} variant="rectangular" width={168} height={315} />
    </>
      }
    </Grid>
  );
}