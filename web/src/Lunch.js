import React from 'react';
import AppBar from '@mui/material/AppBar';
import RestaurantIcon from '@mui/icons-material/Restaurant';
import CssBaseline from '@mui/material/CssBaseline';
import { Box } from '@mui/material';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { ThemeProvider, createTheme, useColorScheme } from '@mui/material/styles';
import IconButton from '@mui/material/IconButton';
import ContrastIcon from '@mui/icons-material/Contrast';
import CircleIcon from '@mui/icons-material/Circle';
import CircleOutlinedIcon from '@mui/icons-material/CircleOutlined';
import Link from '@mui/material/Link';

import { isDev } from './Constants'
import RestaurantListComponent from './RestaurantList';

const theme = createTheme({
  colorSchemes: {
    dark: true,
  },
});

export function getCurrentDate(){
  let newDate = new Date()
  let year = newDate.getFullYear();
  let month = ("0" + (newDate.getMonth() + 1)).slice(-2);
  let date = ("0" + newDate.getDate()).slice(-2);
  let hour = ("0" + newDate.getHours()).slice(-2);
  let minute = ("0" + newDate.getMinutes()).slice(-2);
  let second = ("0" + newDate.getSeconds()).slice(-2);

  return `${year}-${month}-${date} ${hour}:${minute}:${second}`
};

function Lunch() {
  const { mode, setMode } = useColorScheme();
  if (!mode) {
    return null;
  }
  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="relative" color="primary">
        <Toolbar>
          <RestaurantIcon sx={{ marginRight: theme.spacing(2) }} />
          <Typography variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
            Lunch Picker
          </Typography>
          <IconButton aria-label="theme" color="inherit" onClick={() => {
            mode === "system" ? (
              setMode("light")
            ) : (
              mode === "light" ? (
                setMode("dark")
              ) : (
                setMode("system")
              )
            )
          }}>
            {
              mode === "system" ? (
                <ContrastIcon />
              ) : (
                mode === "dark" ? (
                  <CircleOutlinedIcon />
                ) : (
                  <CircleIcon />
                )
              )
            }
          </IconButton>
        </Toolbar>
      </AppBar>
      <main>
        <Box sx={{ padding: theme.spacing(4, 0) }}>
          <RestaurantListComponent />
        </Box>
      </main>
      {/* Footer */}
      <Box sx={{ padding: theme.spacing(8, 0) }}>
      <footer>
        <Typography variant="body2" color="textSecondary" align="center">
          {'Page loaded at ' + getCurrentDate() + '.'}
        </Typography>
        <Typography variant="body2" color="textSecondary" align="center">
          {'Please visit '}
          <Link color="primary" href="https://github.com/jdobes/lunch" target="_blank" rel="noreferrer">
            https://github.com/jdobes/lunch
          </Link>
          {' if you want to improve this app.'}
        </Typography>
        <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
          Enjoy your meal and have a nice day!
        </Typography>
        {isDev ? (
          <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
            WARNING: THIS IS DEV BUILD.
          </Typography>
        ) : (null)}
      </footer>
      </Box>
      {/* End footer */}
    </React.Fragment>
  );
}

export default function ThemedApp() {
  return (
    <ThemeProvider theme={theme}>
      <Lunch />
    </ThemeProvider>
  );
}
