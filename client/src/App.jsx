import './App.css';
import Layout from "./Layout";
import * as React from "react";
import NoMatch from "./pages/nomatch";
import Home from "./pages/home";
import Popular from "./pages/popular";
import Movie from "./pages/movie/movie";
import Favorites from "./pages/favorite";
import { Routes, Route } from "react-router-dom";
import Movies from "./pages/moviesSearch/moviesSearch";
import { UserContextProvider } from "./contexts/userContext";

export default function App() {
  return (
      <UserContextProvider>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="popular" element={<Popular/>} />
            <Route path="movies" element={<Movies/>} />
            <Route path="movie" element={<Movie/>} />
            <Route path="favorites" element={<Favorites/>} />
            <Route path="*" element={<NoMatch />} />
          </Route>
        </Routes>
      </UserContextProvider>
  );
}


