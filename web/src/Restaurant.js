import React, { Component } from 'react';

import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Chip from '@mui/material/Chip';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import PlaceTwoToneIcon from '@mui/icons-material/PlaceTwoTone';
import Typography from '@mui/material/Typography';

const mapsUrl = "https://mapy.cz/zakladni?q="

export function formatDistance(distance){
  if (distance >= 1000) {
    return `${(distance/1000.0).toFixed(1)} km`
  }
  return `${distance} m`
};

class RestaurantComponent extends Component {
  render() {
      return (
        <Accordion disabled={!this.props.menu}>
          <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel-content"
          id="panel-header"
          >
            <Typography variant="h6" sx={{ flexGrow: 1 }} >{this.props.detail[0]}</Typography>
            <Chip icon={<PlaceTwoToneIcon />} variant="outlined" color="info" onClick={() => { window.open(`${mapsUrl}${this.props.detail[1]},${this.props.detail[2]}`); }} label={
              <Typography>
                 {formatDistance(this.props.detail[3])}
              </Typography>
            }/>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              {this.props.menu && this.props.menu.split("\n").map((item, idx) => (
                <span key={idx}>
                  {item}
                  <br/>
                </span>
              ))}
            </Typography>
          </AccordionDetails>
        </Accordion>
      );
  }
}

export default RestaurantComponent;
