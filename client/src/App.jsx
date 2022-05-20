import * as React from "react";
import Home from "./pages/home";
import Popular from "./pages/popular";
import Movies from "./pages/movies";
import Invoice from "./pages/invoice";
import { Routes, Route } from "react-router-dom";
import './App.css';
import Layout from "./Layout";
import NoMatch from "./pages/nomatch";

export default function App() {
  return (
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="populares" element={<Popular/>} />
            <Route path="movies" element={<Movies/>} />
            {/* <Route path="movies/:invoiceId" element={<Invoice />} /> */}


            <Route path="*" element={<NoMatch />} />
          </Route>
        </Routes>
  );
}


