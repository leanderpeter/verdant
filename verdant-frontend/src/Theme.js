import { createMuiTheme } from '@material-ui/core/styles';
import { colors } from '@material-ui/core';

const white = '#FFFFFF';
const black = '#000000';
const darkgrey = '#808080';

// A custom theme for this app
const theme = createMuiTheme({
  palette: {
    black,
    white,
    darkgrey,
    primary: {
      contrastText: black,
      dark: '#ffffff',
      main: '#ffffff',
      light: '#ffffff'
    },
    secondary: {
      contrastText: white,
      dark: '#e1f4f3',
      main: '#e1f4f3',
      light: '#e1f4f3'
    },
    success: {
      contrastText: white,
      dark: '#c7ffd8',
      main: '#c7ffd8',
      light: '#c7ffd8'
    },
    info: {
      contrastText: white,
      dark: colors.blue[900],
      main: colors.blue[600],
      light: colors.blue[400]
    },
    warning: {
      contrastText: white,
      dark: colors.orange[900],
      main: colors.orange[600],
      light: colors.orange[400]
    },
    error: {
      contrastText: white,
      dark: colors.red[900],
      main: colors.red[600],
      light: colors.red[400]
    },
    text: {
      primary: colors.blueGrey[800],
      secondary: colors.blueGrey[600],
      link: colors.blue[600]
    },
    background: {
      default: '#F4F6F8',
      paper: white
    },
    icon: colors.blueGrey[600],
    divider: colors.grey[200]
  }, 
});


// A custom theme for this app
// const theme = createMuiTheme({
//   palette: {
//     primary: {
//       main: '#556cd6',
//     },
//     secondary: {
//       main: '#19857b',
//     },
//     error: {
//       main: red.A400,
//     },
//     background: {
//       default: '#fff',
//     },
//   },
// });


export default theme;