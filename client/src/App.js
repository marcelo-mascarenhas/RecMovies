import * as React from "react";
import Home from "./pages/home/home";
import About from "./pages/about/about";
import Recentes from "./pages/recentes/recentes";
import Navbar from "./components/navbar/navbar";
import { Routes, Route, Outlet, Link } from "react-router-dom";
import './App.css';

// function App (){
//   return (
//     // <UserContextProvider>
//     <Router history={history}>
//       <div id="page-container">
//         <Navbar />
//         <div className="page-body">
//         <Switch>
//           <Route exact path="/pesquisar" component={Pesquisar} />
//         </Switch>
//         </div>
//       </div>
//     </Router>
//     // </UserContextProvider>
//   )
// }


export default function App() {
  return (
      <Routes>
        <Route path="/" element={<Layout />}>
          
          <Route index element={<Home />} />
          <Route path="about" element={<About />} />
          <Route path="recentes" element={<Recentes />} />

          <Route path="*" element={<NoMatch />} />
        </Route>
      </Routes>
  );
}

function Layout() {
  return (
    <div id="page-container">
      {/* <div id="page-container"> */}
        <Navbar />
        <div className="page-body">
          <Outlet />
        </div>
      {/* </div> */}

    </div>
  );
}

function NoMatch() {
  return (
    <div>
      <h2>Nothing to see here!</h2>
      <p>
        <Link to="/">Go to the home page</Link>
      </p>
    </div>
  );
}