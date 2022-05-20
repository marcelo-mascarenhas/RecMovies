import * as React from "react";
import Home from "./pages/home";
import Sobre from "./pages/sobre";
import Recentes from "./pages/recentes";
import YouTube from "./pages/youtube";
import { Routes, Route } from "react-router-dom";
import './App.css';
import Layout from "./Layout";
import NoMatch from "./pages/nomatch";

export default function App() {
  return (
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="sobre" element={<Sobre />} />
            <Route path="recentes" element={<YouTube />} />

            <Route path="*" element={<NoMatch />} />
          </Route>
        </Routes>
  );
}


