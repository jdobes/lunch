import React, { Component } from 'react';
import Container from '@mui/material/Container';

import RestaurantComponent from './Restaurant';
import LoadingCircleComponent from './LoadingCircle';

import { config } from './Constants'

class RestaurantListComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      availableRestaurants: [],
      restaurantNameMap: {},
      todaysMenus: []
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });
    Promise.all([fetch(config.API_URL + '/api/restaurants'), fetch(config.API_URL + '/api/menus')])
      .then(([responseRestaurants, responseMenus]) => {
        return Promise.all([responseRestaurants.json(), responseMenus.json()])
      })
      .then(([responseRestaurants, responseMenus]) => {
        // Setup restaurant label -> name map
        const newRestaurantNameMap = {}
        for (const restaurantObject of responseRestaurants.restaurants.values()) {
          newRestaurantNameMap[restaurantObject.label] = restaurantObject.name
        }
        this.setState({ availableRestaurants: responseRestaurants.restaurants,
                        restaurantNameMap: newRestaurantNameMap,
                        todaysMenus: responseMenus.menus,
                        isLoading: false })
      });
  }

  render() {
    const { isLoading, restaurantNameMap, todaysMenus } = this.state;
    if (isLoading || todaysMenus.length === 0) {
      return (
        <Container maxWidth="md">
          <LoadingCircleComponent />
        </Container>
      );
    }
    const restaurantPanels = []
    for (const value of todaysMenus.values()) {
      restaurantPanels.push(<RestaurantComponent key={value.restaurant} name={restaurantNameMap[value.restaurant]} menu={value.menu}/>)
    }
    return (
      <Container maxWidth="md">
        {restaurantPanels}
      </Container>
    );
  }
}

export default RestaurantListComponent;
