import * as React from 'react';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import {useLocation} from 'react-router-dom';
import Skeleton from '@mui/material/Skeleton';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import { Card, CardContent, CardMedia } from '@mui/material';

const NUM_FILMES = 2

const data = [
  {
    src: 'https://source.unsplash.com/random',
    title: 'Doutor Estranho no multiverso da loucura',
    channel: '22 maio, 2022',
    views: '396 k views',
  },
  {
    src: 'https://source.unsplash.com/random',
    title: 'Sonic 2 o filme',
    channel: 'Calvin Harris',
    views: '130 M views',
  },
];

function Media(props) {
  const { loading } = props;
  return (
    <Container sx={{ py: 8 }} maxWidth="md">
        <Grid container spacing={2}>
        {(loading ? Array.from(new Array(NUM_FILMES)) : data).map((filme, index) => (
            <Grid item key={index} xs={12} sm={6} md={4}>
            <Card
                sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
            >

            {/* Image */}
            {filme ? (
                <CardMedia
                    component="img"
                    // sx={{
                    //   // 16:9
                    //   pt: '56.25%',
                    // }}
                    image={filme.src}
                    alt={filme.title}
                  />
                ) : (
                <Skeleton variant="rectangular" height={200} />
            )}

            {/* Descrição */}
            {filme ? (
                <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="body2">
                        {filme.title}
                    </Typography>
                    <Typography display="block" variant="caption" color="text.secondary">
                        {filme.channel}
                    </Typography>
                </CardContent>
                ) : (
                <CardContent sx={{ flexGrow: 1 }}>
                    <Skeleton />
                    <Skeleton width="30%" />
                </CardContent>
            )}

            </Card>
            </Grid>
        ))}
        </Grid>
    </Container>
  );
}

export default function Movies() {
  
  const location = useLocation();

  if (location.state){
    var moviesInfos = location.state
    console.log(moviesInfos)
  }

  return (
    <Box sx={{ overflow: 'hidden' }}>
      <Media loading={true} />
      <Media />
    </Box>
  );
}