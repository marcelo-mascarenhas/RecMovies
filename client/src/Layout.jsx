import { Outlet } from "react-router-dom";
import Navbar from "./components/navbar";
import CssBaseline from '@mui/material/CssBaseline';
import { ThemeProvider, createTheme } from '@mui/material/styles';
// import Footer from "./components/footer";

const creme = '#E9E7D1'
const azul = "#314E55"
const cinza = '#D8D8D8'


const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#FA9F42',
    },
    secondary: {
      main: '#FA9F42',
    },
  },
  components: {
    MuiAppBar: {
      styleOverrides: {
        colorPrimary: {
          backgroundColor: '#121212'
        }
      }
    },
  }
});

export default function Layout() {
    return (
      <ThemeProvider theme={theme}>
        <Navbar></Navbar>
        <CssBaseline />
        <Outlet />
        {/* <Footer></Footer> */}
      </ThemeProvider>

    )
  }