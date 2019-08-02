import React, { Component } from 'react';

import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Typography from '@material-ui/core/Typography';

class RestaurantComponent extends Component {
  render() {
      return (
        <ExpansionPanel disabled={!this.props.menu}>
          <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel-content"
          id="panel-header"
          >
            <Typography variant="h6">{this.props.name}</Typography>
          </ExpansionPanelSummary>
          <ExpansionPanelDetails>
            <Typography>
              {this.props.menu && this.props.menu.split("\n").map((item) => (
                <span>
                  {item}
                  <br/>
                </span>
              ))}
            </Typography>
          </ExpansionPanelDetails>
        </ExpansionPanel>
      );
  }
}

export default RestaurantComponent;
