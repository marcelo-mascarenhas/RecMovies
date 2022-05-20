import * as React from 'react';
import { useEffect, useState } from "react";
import useForm from "../hooks/useForm";
import Button from '@mui/material/Button';
import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Link from '@mui/material/Link';
import SearchIcon from '@mui/icons-material/Search';

import { useNavigate } from "react-router-dom";

import { Divider, IconButton, InputBase, Paper, TextField } from '@mui/material';

import { popularMovies } from "../services/movies/popularMovies";

import { getMovieInfo } from "../services/movies/getMovie";


async function getPopularMovies(farm_id) {
  try {
    const animals_response = await popularMovies(farm_id);
    console.log(animals_response, "teste")

  } catch (err) {
    console.log("Error fetching movies");
  }
}

function Copyright() {
  return (
    <Typography variant="body2" color="text.secondary" align="center">
      {'Copyright © '}
      {/* <Link color="inherit" href="https://mui.com/">
        Your Website
      </Link>{' '} */}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const cards = [1, 2, 3];

export default function Home() {

  const navigateTo = useNavigate()

  const {
    values,
    errors,
    handleChange,
    handleSelectChange,
    handleSubmit,
    handleSetErrors,
  } = useForm();

  useEffect(() => {
    const x = getPopularMovies();
  }, []);

  async function checkValues(){
    const error = {};
    return error;
  }

  async function valuesAreCorrect(){
    console.log("mandando pro back:", values.searchMovie)

    try{
      var movieInfos
      movieInfos= await getMovieInfo(values.searchMovie)
    }
    catch(err){
      console.log("fail api")
    }

  }

  return (
      <main>
        {/* Hero unit */}
        <Box
          sx={{
            bgcolor: 'background.paper',
            pt: 8,
            pb: 6,
          }}
          >
          <Container maxWidth="sm">
            <Typography
              component="h1"
              variant="h2"
              align="center"
              color="text.primary"
              gutterBottom
            >
             Bem vindo.
            </Typography>
            <Typography variant="h6" align="center" color="text.secondary" paragraph>
              Milhões de filmes para descobrir. <nobr>Explore agora! </nobr>
            </Typography>

            <Paper
              onSubmit={handleSubmit(checkValues, valuesAreCorrect)}
              component="form"
              align="center"
              sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: "sm" }}
            >
              <InputBase
                sx={{ ml: 1, flex: 1 }}
                // name = "searchMovie"
                id = "searchMovie"
                placeholder="Search"
                inputProps={{ 'aria-label': 'search google maps' }}
                value= {values.searchMovie || ''}
                onChange={handleChange}
                // onChange={}
              />
              <IconButton type="submit" sx={{ p: '10px' }} aria-label="search">
                <SearchIcon />
              </IconButton>

            </Paper>

          </Container>
        </Box>
        <Container sx={{ py: 8 }} maxWidth="md">
          {/* End hero unit */}
          <Grid container spacing={2}>
            {cards.map((card) => (
              <Grid item key={card} xs={12} sm={6} md={4}>
                <Card
                  sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}
                >
                  <CardMedia
                    component="img"
                    // sx={{
                    //   // 16:9
                    //   pt: '56.25%',
                    // }}
                    image="https://source.unsplash.com/random"
                    alt="random"
                    
                  />
                  <CardContent sx={{ flexGrow: 1 }}>
                    <Typography gutterBottom variant="h5" component="h2">
                      Heading
                    </Typography>
                    <Typography variant="subtitle2">
                      Apr 20, 2022
                    </Typography>
                  </CardContent>
                  {/* <CardActions>
                    <Button size="small">View</Button>
                    <Button size="small">Edit</Button>
                  </CardActions> */}
                </Card>
              </Grid>
            ))}
          </Grid>
        </Container>
      </main>
  );
}