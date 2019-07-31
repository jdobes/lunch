import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import CircularProgress from '@material-ui/core/CircularProgress';

const useStyles = makeStyles(theme => ({
  progress: {
    margin: theme.spacing(2),
  },
}));

export default function LoadingCircleComponent() {
  const classes = useStyles();

  return (
    <Grid container justify = "center">
      <CircularProgress className={classes.progress} />
    </Grid>
  );
}
