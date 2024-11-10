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
      isLoading: true,
      restaurantDetailMap: {},
      todaysMenusMap: {},
      defaultUserLocation: {}
    };
  }

  componentDidMount() {
    Promise.all([fetch(config.API_URL + '/api/origins'), fetch(config.API_URL + '/api/restaurants'), fetch(config.API_URL + '/api/menus')])
      .then(([responseOrigins, responseRestaurants, responseMenus]) => {
        return Promise.all([responseOrigins.json(), responseRestaurants.json(), responseMenus.json()])
      })
      .then(([responseOrigins, responseRestaurants, responseMenus]) => {
        // Setup origin label -> detail map
        const originDetailMap = {}
        for (const originObject of responseOrigins.origins.values()) {
          originDetailMap[originObject.label] = { name: originObject.name, latitude: originObject.latitude, longitude: originObject.longitude }
        }
        // Setup restaurant label -> detail map
        const restaurantDetailMap = {}
        for (const restaurantObject of responseRestaurants.restaurants.values()) {
          restaurantDetailMap[restaurantObject.label] = { name: restaurantObject.name, latitude: restaurantObject.latitude, longitude: restaurantObject.longitude }
        }
        // Setup restaurant label -> menus map
        const todaysMenusMap = {}
        for (const menuObject of responseMenus.menus) {
          todaysMenusMap[menuObject.restaurant] = menuObject.menu
        }
        this.setState({ restaurantDetailMap: restaurantDetailMap,
                        todaysMenusMap: todaysMenusMap,
                        defaultUserLocation: { latitude: originDetailMap["office"].latitude, longitude: originDetailMap["office"].longitude },
                        isLoading: false })
      });
  }

  render() {
    const { isLoading, restaurantDetailMap, todaysMenusMap, defaultUserLocation } = this.state;
    if (isLoading || todaysMenusMap.length === 0) {
      return (
        <Container maxWidth="md">
          <LoadingCircleComponent />
        </Container>
      );
    }
    let originLocation = defaultUserLocation
    if (this.props.userLocation !== null) {  // Real position available
      originLocation = this.props.userLocation
    }
    // Calculate current distances
    const restaurantDistanceMap = {}
    for (const restaurant in restaurantDetailMap) {
      restaurantDistanceMap[restaurant] = getDistance(
        { latitude: originLocation.latitude, longitude: originLocation.longitude},
        { latitude: restaurantDetailMap[restaurant].latitude, longitude: restaurantDetailMap[restaurant].longitude})
    }
    // Sort restaurants
    const sortedRestaurants = Object.keys(restaurantDistanceMap)
    sortedRestaurants.sort((a, b) => {
      return restaurantDistanceMap[a] - restaurantDistanceMap[b]
    })

    const restaurantPanels = []
    for (const restaurant of sortedRestaurants) {
      restaurantPanels.push(<RestaurantComponent key={restaurant} detail={restaurantDetailMap[restaurant]} distance={restaurantDistanceMap[restaurant]} menu={todaysMenusMap[restaurant]}/>)
    }
    return (
      <Container maxWidth="md">
        {restaurantPanels}
      </Container>
    );
  }
}

export default RestaurantListComponent;
