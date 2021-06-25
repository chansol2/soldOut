import classes from "./NavigationBar.module.css";

import Profile from "./components/NavComp/Profile";
import Menu from "./components/NavComp/Menu";
import Logout from "./components/NavComp/Logout";

const NavigationBar = () => {
  return (
    <div className={classes.container}>
      <Profile />
      <Menu />
      <Logout />
    </div>
  );
};

export default NavigationBar;
