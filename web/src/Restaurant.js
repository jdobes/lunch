import React, { Component } from 'react';

import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Typography from '@mui/material/Typography';

class RestaurantComponent extends Component {
  render() {
      return (
        <Accordion disabled={!this.props.menu}>
          <AccordionSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel-content"
          id="panel-header"
          >
            <Typography variant="h6">{this.props.name}</Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              {this.props.menu && this.props.menu.split("\n").map((item) => (
                <span>
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
