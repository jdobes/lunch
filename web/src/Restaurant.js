import React, { Component } from 'react';

import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Typography from '@material-ui/core/Typography';

class RestaurantComponent extends Component {
  render() {
      return (
          <ExpansionPanel disabled>
              <ExpansionPanelSummary
              expandIcon={<ExpandMoreIcon />}
              aria-controls="panel-content"
              id="panel-header"
              >
              <Typography>Disabled Expansion Panel</Typography>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
              <Typography>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse malesuada lacus ex,
                  sit amet blandit leo lobortis eget.
              </Typography>
              </ExpansionPanelDetails>
            </ExpansionPanel>
      );
  }
}

export default RestaurantComponent;
