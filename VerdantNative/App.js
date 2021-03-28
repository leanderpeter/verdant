import React from "react";
import { Text } from "react-native";
import { createBottomTabNavigator, createAppContainer } from "react-navigation";
import styles from "./assets/styles";
import HomeScreen from "./containers/Home";
import Icon from "./components/Icon";

export default function App() {
    return (
        <HomeScreen/>
    );
  };

/*
const App = createBottomTabNavigator(
	{
		Explore: {
			screen: HomeScreen,
			navigationOptions: {
				tabBarIcon: ({ focused }) => {
					const iconFocused = focused ? "#7444C0" : "#363636";
					return (
						<Text style={[styles.iconMenu, { color: iconFocused }]}>
							<Icon name="explore" />
						</Text>
					);
				}
			}
		},
		
	}
);

export default createAppContainer(App);
*/