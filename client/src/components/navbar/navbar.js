  import { useState } from 'react';
  import { Link } from "react-router-dom";
  import useForm from '../../hooks/useForm';
  import search_icon from '../../assets/search-icon.svg';

  import './navbar.css';

  function Navbar() {
    const { values, errors, handleChange, handleSelectChange, handleSelectStateChange, handleSubmit, handleSetErrors } = useForm();

    const [isSidenavOpen, setIsSidenavOpen] = useState(false);

    return (
      <>
        <nav className="navbar">
          {/* <img src={search_icon} alt="Logo" onClick={() => history.push('/your-properties')}/> */}
            {/* <span onClick={() => console.log('/home')}>  Home </span> */}
            <Link to="/">Home</Link>
          <div>
            <Link to="/recentes">Filmes recentes</Link>
            <Link to="/about">About</Link>
          </div>
          <div className="option search_icon" onClick={() => {console.log('/pesquisar')}}>
            <img src={search_icon} alt="Icone de Busca"/>
          </div>


          <div className="sandwich-icon" onClick={() => setIsSidenavOpen(true)}>
            <div/>
            <div/>
            <div/>
          </div>
        </nav>

        <div className={"sidenav " + (isSidenavOpen ? "open" : "close")}>
          <div className="close" onClick={() => setIsSidenavOpen(false)}>&times;</div>
            <span className="option" onClick={() => console.log('/')}>Pesquisa</span>
            <span className="option" onClick={() => console.log('/')}>Filmes</span>
            {/* <span className="option">FAQ</span> */}
            <span className="option" onClick={() => {console.log('/')}}>Sair</span>
        </div>
      </>
    )
  }

  export default Navbar;


//   <nav>
//   <ul>
//     <li>
//       <Link to="/">Home</Link>
//     </li>
//     <li>
//       <Link to="/about">About</Link>
//     </li>
//   </ul>
// </nav>