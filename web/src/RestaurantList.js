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
      restaurantDetailMap: {},
      originDetailMap: {},
      todaysMenus: []
    };
  }

  componentDidMount() {
    this.setState({ isLoading: true });
    Promise.all([fetch(config.API_URL + '/api/origins'), fetch(config.API_URL + '/api/restaurants'), fetch(config.API_URL + '/api/menus')])
      .then(([responseOrigins, responseRestaurants, responseMenus]) => {
        return Promise.all([responseOrigins.json(), responseRestaurants.json(), responseMenus.json()])
      })
      .then(([responseOrigins, responseRestaurants, responseMenus]) => {
        // Setup origin label -> detail map
        const newOriginDetailMap = {}
        for (const originObject of responseOrigins.origins.values()) {
          newOriginDetailMap[originObject.label] = [originObject.name, originObject.latitude, originObject.longitude]
        }
        // Setup restaurant label -> detail map
        const newRestaurantDetailMap = {}
        for (const restaurantObject of responseRestaurants.restaurants.values()) {
          newRestaurantDetailMap[restaurantObject.label] = [restaurantObject.name, restaurantObject.latitude, restaurantObject.longitude]
        }
        this.setState({ availableRestaurants: responseRestaurants.restaurants,
                        originDetailMap: newOriginDetailMap,
                        restaurantDetailMap: newRestaurantDetailMap,
                        todaysMenus: responseMenus.menus,
                        isLoading: false })
      });
  }

  render() {
    const { isLoading, restaurantDetailMap, originDetailMap, todaysMenus } = this.state;
    if (isLoading || todaysMenus.length === 0) {
      return (
        <Container maxWidth="md">
          <LoadingCircleComponent />
        </Container>
      );
    }
    const restaurantPanels = []
    for (const value of todaysMenus.values()) {
      restaurantPanels.push(<RestaurantComponent origin={originDetailMap["office"]} key={value.restaurant} detail={restaurantDetailMap[value.restaurant]} menu={value.menu}/>)
    }
    return (
      <Container maxWidth="md">
        {restaurantPanels}
      </Container>
    );
  }
}

export default RestaurantListComponent;
