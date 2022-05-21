import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import Typography from '@mui/material/Typography';
import Menu from '@mui/material/Menu';
import MenuIcon from '@mui/icons-material/Menu';
import Container from '@mui/material/Container';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import Tooltip from '@mui/material/Tooltip';
import MenuItem from '@mui/material/MenuItem';
import MovieCreationIcon from '@mui/icons-material/MovieCreation';
import { Link } from 'react-router-dom';
import SLink from './slink';

const pages = ['popular'];

const settings = ['Favoritos'];

const Navbar = () => {
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Typography
          
            variant="h6"
            noWrap
            component="div"
            sx={{ mr: 2, display: { xs: 'none', md: 'flex' }, alignItems: 'center', }}
            >
            <MovieCreationIcon></MovieCreationIcon>
            <SLink to="/">MovieRec</SLink>
          </Typography>
          <Box sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' } }}>
            <IconButton
              size="large"
              aria-label="account of current user"
              aria-controls="menu-appbar"
              aria-haspopup="true"
              onClick={handleOpenNavMenu}
              color="inherit"
            >
              <MenuIcon />
            </IconButton>
            <Menu
              id="menu-appbar"
              anchorEl={anchorElNav}
              anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'left',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'left',
              }}
              open={Boolean(anchorElNav)}
              onClose={handleCloseNavMenu}
              sx={{
                display: { xs: 'block', md: 'none' },
              }}
            >
              {pages.map((page) => (
                <MenuItem key={page} onClick={handleCloseNavMenu}>
                  <SLink to={"/"+ page}><Typography textAlign="center">{page}</Typography></SLink>
                </MenuItem>
              ))}
            </Menu>
          </Box>

          <Typography
            variant="h6" noWrap component="div"
            sx={{ flexGrow: 1, display: { xs: 'flex', md: 'none' }, alignItems: 'center' }}>
            <MovieCreationIcon></MovieCreationIcon>
            MovieRec
          </Typography>
          
          
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            {pages.map((page) => (
              <Button
                key={page}
                onClick={handleCloseNavMenu}
                component={Link} 
                to={'/' + page}
                sx={{ my: 2, color: 'white', display: 'block' }}
              >
                {page}
                {/* <Link to="/about">About</Link> */}
                
              </Button>
            ))}
          </Box>

          <Box sx={{ flexGrow: 0 }}>
            <Tooltip title="Open settings">
              <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
              </IconButton>
            </Tooltip>
            <Menu
              sx={{ mt: '45px' }}
              id="menu-appbar"
              anchorEl={anchorElUser}
              anchorOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
              }}
              open={Boolean(anchorElUser)}
              onClose={handleCloseUserMenu}
            >
              {settings.map((setting) => (
                <MenuItem key={setting} onClick={handleCloseUserMenu}>
                  <Typography textAlign="center">{setting}</Typography>
                </MenuItem>
              ))}
            </Menu>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
export default Navbar;
    // <>
    //   <nav className="navbar">
    //     {/* <img src={search_icon} alt="Logo" onClick={() => history.push('/your-properties')}/> */}
    //       {/* <span onClick={() => console.log('/home')}>  Home </span> */}
    //       <Link to="/">Home</Link>
    //     <div>
    //       <Link to="/recentes">Filmes recentes</Link>
    //       <Link to="/about">About</Link>
    //     </div>
    //     <div className="option search_icon" onClick={() => {console.log('/pesquisar')}}>
    //       <img src={search_icon} alt="Icone de Busca"/>
    //     </div>


    //     <div className="sandwich-icon" onClick={() => setIsSidenavOpen(true)}>
    //       <div/>
    //       <div/>
    //       <div/>
    //     </div>
    //   </nav>

    //   <div className={"sidenav " + (isSidenavOpen ? "open" : "close")}>
    //     <div className="close" onClick={() => setIsSidenavOpen(false)}>&times;</div>
    //       <span className="option" onClick={() => console.log('/')}>Pesquisa</span>
    //       <span className="option" onClick={() => console.log('/')}>Filmes</span>
    //       {/* <span className="option">FAQ</span> */}
    //       <span className="option" onClick={() => {console.log('/')}}>Sair</span>
    //   </div>
    // </>
