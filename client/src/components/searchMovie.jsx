import * as React from 'react';
import Typography from '@mui/material/Typography';
import SearchIcon from '@mui/icons-material/Search';
import { useNavigate } from "react-router-dom";

import { Divider, IconButton, InputBase, Paper, TextField } from '@mui/material';

export default function SearchMovie() {

  const navigateTo = useNavigate()
  const [value, setValue] = React.useState("");

  const handleChange = (event) => {
    setValue(event.currentTarget.value)
  };

  const handleSubmit = () => async (event) => {
    event.preventDefault();
    console.log('teste')
    navigateTo("/movies", {state:{value}})
  };

  return (
    <Paper
      onSubmit={handleSubmit()}
      component="form"
      align="center"
      sx={{ p: '2px 4px', mb:1, display: 'flex', alignItems: 'center', width: "sm" }}
    >
      <InputBase
        sx={{ ml: 1, flex: 1 }}
        // name = "searchMovie"
        id = "searchMovie"
        placeholder="Search"
        inputProps={{ 'aria-label': 'search google maps' }}
        value= {value || ''}
        onChange={handleChange}
        // onChange={}
      />
      <IconButton type="submit" sx={{ p: '10px' }} aria-label="search">
        <SearchIcon />
      </IconButton>
    </Paper>

  );
}