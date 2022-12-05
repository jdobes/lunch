import React from 'react';
import Grid from '@mui/material/Grid';
import { createTheme } from '@mui/material/styles';
import CircularProgress from '@mui/material/CircularProgress';

const theme = createTheme();

export default function LoadingCircleComponent() {
  return (
    <Grid container justifyContent = "center">
      <CircularProgress sx={{ margin: theme.spacing(2) }} />
    </Grid>
  );
}
