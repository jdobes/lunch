import React, { Component } from 'react';
import Container from '@mui/material/Container';

import { getDistance } from 'geolib';

import RestaurantComponent from './Restaurant';
import LoadingCircleComponent from './LoadingCircle';
import { config } from './Constants'

class RestaurantListComponent extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      restaurantDetailMap: {},
      todaysMenusMap: {}
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
        const originDetailMap = {}
        for (const originObject of responseOrigins.origins.values()) {
          originDetailMap[originObject.label] = [originObject.name, originObject.latitude, originObject.longitude]
        }
        // Setup restaurant label -> detail map
        const newRestaurantDetailMap = {}
        for (const restaurantObject of responseRestaurants.restaurants.values()) {
          const distance = getDistance(
            { latitude: originDetailMap["office"][1], longitude: originDetailMap["office"][2] },
            { latitude: restaurantObject.latitude, longitude: restaurantObject.longitude }
          )
          newRestaurantDetailMap[restaurantObject.label] = [restaurantObject.name, restaurantObject.latitude, restaurantObject.longitude, distance]
        }
        // Setup restaurant label -> menus map
        const newtodaysMenusMap = {}
        for (const menuObject of responseMenus.menus) {
          newtodaysMenusMap[menuObject.restaurant] = menuObject.menu
        }
        this.setState({ restaurantDetailMap: newRestaurantDetailMap,
                        todaysMenusMap: newtodaysMenusMap,
                        isLoading: false })
      });
  }

  render() {
    const { isLoading, restaurantDetailMap, todaysMenusMap } = this.state;
    if (isLoading || todaysMenusMap.length === 0) {
      return (
        <Container maxWidth="md">
          <LoadingCircleComponent />
        </Container>
      );
    }
    // Sort restaurants
    const sortedRestaurants = Object.keys(restaurantDetailMap)
    sortedRestaurants.sort((a, b) => {
      return restaurantDetailMap[a][3] - restaurantDetailMap[b][3]
    })

    const restaurantPanels = []
    for (const restaurant of sortedRestaurants) {
      restaurantPanels.push(<RestaurantComponent key={restaurant} detail={restaurantDetailMap[restaurant]} menu={todaysMenusMap[restaurant]}/>)
    }
    return (
      <Container maxWidth="md">
        {restaurantPanels}
      </Container>
    );
  }
}

export default RestaurantListComponent;
