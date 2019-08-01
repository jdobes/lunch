import React from 'react';
import AppBar from '@material-ui/core/AppBar';
import RestaurantIcon from '@material-ui/icons/Restaurant';
import CssBaseline from '@material-ui/core/CssBaseline';

import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Link from '@material-ui/core/Link';

import RestaurantListComponent from './RestaurantList';

const useStyles = makeStyles(theme => ({
  icon: {
    marginRight: theme.spacing(2),
  },
  content: {
    padding: theme.spacing(4, 0),
  },
  footer: {
    padding: theme.spacing(8, 0),
  },
}));

export default function Lunch() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <AppBar position="relative" color="primary">
        <Toolbar>
          <RestaurantIcon className={classes.icon} />
          <Typography variant="h6" color="inherit" noWrap>
            Lunch Picker
          </Typography>
        </Toolbar>
      </AppBar>
      <main>
        <div className={classes.content}>
          <RestaurantListComponent />
        </div>
      </main>
      {/* Footer */}
      <footer className={classes.footer}>
        <Typography variant="subtitle1" align="center" color="textSecondary" component="p">
          Enjoy your meal and have a nice day!
        </Typography>
        <Typography variant="body2" color="textSecondary" align="center">
          {'Please visit '}
          <Link color="primary" href="https://github.com/jdobes/lunch" target="_blank" rel="noreferrer">
            https://github.com/jdobes/lunch
          </Link>
          {' if you want to improve this app.'}
        </Typography>
      </footer>
      {/* End footer */}
    </React.Fragment>
  );
}
