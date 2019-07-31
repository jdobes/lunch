import React, { Component } from 'react';
import Container from '@material-ui/core/Container';

import RestaurantComponent from './Restaurant';
import LoadingCircleComponent from './LoadingCircle';

const API = 'http://localhost:8000'

class RestaurantListComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      data: null,
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });
    fetch(API + '/api/restaurants')
      .then(response => response.json())
      .then(data => this.setState({ data, isLoading: false }));
  }

  render() {
    const { isLoading, data } = this.state;
    if (isLoading) {
      return (
        <Container maxWidth="md">
          <LoadingCircleComponent />
        </Container>
      );
    }
    return (
      <Container maxWidth="md">
        <RestaurantComponent />
        <RestaurantComponent />
        <RestaurantComponent />
      </Container>
    );
  }
}

export default RestaurantListComponent;
